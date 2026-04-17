from generated.IfElseLangVisitor import IfElseLangVisitor
from generated.IfElseLangParser import IfElseLangParser
from .SymbolTable import SymbolTable, Symbol
from .IR_Generator import IR_Generator  # <-- IMPORTANTE: Importar el generador de IR

class SemanticVisitor(IfElseLangVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self.current_function = None
        self.ir = IR_Generator()  # <-- INSTANCIA DEL GENERADOR DE IR

    # Visitante para la declaración de variables.
    def visitDeclaration(self, ctx:IfElseLangParser.DeclarationContext):
        var_name = ctx.ID().getText()
        type_name = ctx.type_().getText()
        symbol = Symbol(name=var_name, type=type_name, category='variable')
        
        self.table.insert(var_name, symbol)

        # Si hay una expresión de inicialización, la validamos y generamos IR.
        if ctx.expr():
            # 1. Visitar la expresión para obtener su tipo y su "dirección" (temporal/variable)
            expr_addr = self.visit(ctx.expr()) # Ahora devuelve (tipo, addr)
            expr_type = expr_addr[0] # Extraemos el tipo
            expr_val_addr = expr_addr[1] # Extraemos la dirección del valor
            
            if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
                print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a la variable '{var_name}' de tipo '{symbol.type}' en su declaración.")
            
            # 2. Generar la instrucción TAC de asignación
            self.ir.add_instruction('=', expr_val_addr, result=var_name)
        
        return None

    # --- Visitante para la declaración de funciones ---
    def visitFunctionDecl(self, ctx:IfElseLangParser.FunctionDeclContext):
        func_name = ctx.ID().getText()
        return_type = ctx.type_().getText()
        
        # 1. Crear un nuevo bloque de función en el IR
        # Esto genera una etiqueta para el inicio de la función
        function_start_label = self.ir.new_label()
        self.ir.add_instruction(f"FUNCTION {func_name}:") # Marcar el inicio de la función
        self.ir.add_instruction(f"{function_start_label}:")

        # 2. Procesar parámetros
        param_symbols = []
        param_addrs = [] # Para pasar a la llamada
        if ctx.paramList():
            for param_ctx in ctx.paramList().param():
                param_name = param_ctx.ID().getText()
                param_type = param_ctx.type_().getText()
                param_symbols.append(Symbol(name=param_name, type=param_type, category='variable'))
                param_addrs.append((param_name, param_type)) # Guardar nombre y tipo del parámetro

        # 3. Crear el símbolo de la función
        func_symbol = Symbol(name=func_name, type=return_type, category='function', params=param_symbols)
        self.table.insert(func_name, func_symbol)

        # 4. Guardar referencia a la función actual para validar retornos y IR
        self.current_function = func_symbol
        
        # 5. Entrar en un nuevo ámbito para el cuerpo de la función
        self.table.enter_scope()

        # 6. Definir los parámetros como variables en el nuevo ámbito
        # También "copiamos" los parámetros al ámbito local (si es necesario para convenciones de llamada)
        for param in param_symbols:
            self.table.insert(param.name, param)
            # Podríamos añadir una instrucción para "recibir" el parámetro, ej: param_name = ARG_N
            # self.ir.add_instruction('PARAM_RECEIVE', result=param.name) # Placeholder

        # 7. Visitar el cuerpo de la función
        # self.visitChildren(ctx.block()) # Visitamos el bloque del cuerpo de la función
        # La regla 'block' tiene una lista de statement, la visitamos directamente.
        # No usamos visitChildren(ctx.block()) directamente porque visitamos statement por statement
        # para que cada statement genere su IR.
        for statement_ctx in ctx.block().statement():
            self.visit(statement_ctx)


        # 8. Asegurarse de que funciones no void tengan un return
        if return_type != 'void' and not self._has_return_statement(ctx.block()):
             print(f"Advertencia Semántica: La función '{func_name}' de tipo '{return_type}' no tiene un 'return' explícito en todos los caminos.")
             # Aquí podríamos insertar un return predeterminado o un error de ejecución
             self.ir.add_instruction('RETURN', '0' if return_type == 'int' else '""') # Return por defecto para evitar fallos de ejecución


        # 9. Salir del ámbito de la función
        self.table.exit_scope()
        
        # 10. Limpiar la referencia a la función actual
        self.current_function = None

        # 11. Marcar el fin de la función
        self.ir.add_instruction(f"END FUNCTION {func_name}")
        
        return None

    # --- Función auxiliar para verificar si un bloque tiene un return (muy básico) ---
    def _has_return_statement(self, block_ctx):
        # Esto es una comprobación simple y no considera todos los caminos
        for stmt in block_ctx.statement():
            if isinstance(stmt, IfElseLangParser.ReturnStatementContext):
                return True
            # if isinstance(stmt, IfElseLangParser.IfStatementContext):
            #     if self._has_return_statement(stmt.block(0)) or \
            #        (stmt.block(1) and self._has_return_statement(stmt.block(1))):
            #         return True
        return False

    # --- Visitante para la llamada a funciones ---
    def visitFuncCallExpr(self, ctx:IfElseLangParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        symbol = self.table.lookup(func_name)

        # Comprobaciones semánticas (se mantienen igual)
        if symbol is None:
            print(f"Error Semántico: La función '{func_name}' no ha sido declarada.")
            return ('error_type', None)
        if symbol.category != 'function':
            print(f"Error Semántico: El identificador '{func_name}' no es una función, no se puede llamar.")
            return ('error_type', None)
        
        provided_args = ctx.argList().expr() if ctx.argList() else []
        expected_params = symbol.params
        if len(provided_args) != len(expected_params):
            print(f"Error Semántico: La función '{func_name}' esperaba {len(expected_params)} argumentos, pero recibió {len(provided_args)}.")
            return ('error_type', None)
        
        arg_addrs = [] # Para almacenar las direcciones de los argumentos
        for i, arg_expr in enumerate(provided_args):
            arg_type, arg_addr = self.visit(arg_expr) # Ahora visit devuelve (tipo, addr)
            param_type = expected_params[i].type
            if arg_type != param_type:
                print(f"Error Semántico: En la llamada a '{func_name}', el argumento {i+1} es de tipo '{arg_type}', pero se esperaba '{param_type}'.")
                return ('error_type', None)
            arg_addrs.append(arg_addr)
        
        # Generar IR para la llamada a función
        for addr in arg_addrs:
            self.ir.add_instruction('PARAM', addr) # Pasar cada argumento como un parámetro

        result_temp = None
        if symbol.type != 'void':
            result_temp = self.ir.new_temp()
            self.ir.add_instruction('CALL', func_name, str(len(arg_addrs)), result=result_temp)
            return (symbol.type, result_temp) # Devuelve el tipo y el temporal donde se guarda el resultado
        else:
            self.ir.add_instruction('CALL', func_name, str(len(arg_addrs)))
            return ('void', None) # Las funciones void no devuelven valor ni temporal
            

    # --- Visitante para la sentencia de retorno ---
    def visitReturnStatement(self, ctx:IfElseLangParser.ReturnStatementContext):
        if self.current_function is None:
            print("Error Semántico: La sentencia 'return' solo puede aparecer dentro de una función.")
            return None
        
        return_expr_type, return_expr_addr = self.visit(ctx.expr()) # Visitar la expresión de retorno
        expected_type = self.current_function.type
        
        if return_expr_type != expected_type:
            print(f"Error Semántico: La función '{self.current_function.name}' debe retornar un valor de tipo '{expected_type}', pero se encontró '{return_expr_type}'.")
            
        # Generar IR para el retorno
        self.ir.add_instruction('RETURN', return_expr_addr)
        
        return None
        
    # --- VISITANTES EXISTENTES (CON MODIFICACIONES PARA IR) ---

    def visitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
            return None
        
        if symbol.category == 'function':
            print(f"Error Semántico: No se puede asignar un valor a la función '{var_name}'.")
            return None

        # Obtener tipo y dirección de la expresión
        expr_type, expr_val_addr = self.visit(ctx.expr())
        if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
            print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a la variable '{var_name}' de tipo '{symbol.type}'.")
            
        # Generar IR de asignación
        self.ir.add_instruction('=', expr_val_addr, result=var_name)
        return None

    def visitIdExpr(self, ctx:IfElseLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)
        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
            return ('error_type', None) # Devuelve tupla
        if symbol.category == 'function':
            print(f"Error Semántico: No se puede usar la función '{var_name}' como una variable en una expresión.")
            return ('error_type', None) # Devuelve tupla
        return (symbol.type, var_name) # Devuelve (tipo, nombre_de_variable)

    # REFACTORIZADO: visitIfStatement ahora es mucho más simple gracias a la regla 'block'.
    def visitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        # 1. Visitar la condición para obtener su tipo y dirección
        cond_type, cond_addr = self.visit(ctx.condition())

        # 2. Crear etiquetas para los bloques
        else_label = self.ir.new_label()
        end_label = self.ir.new_label()

        # 3. Generar el salto condicional
        # Si la condición es falsa, salta al bloque ELSE (o al final si no hay else)
        target_label = else_label if ctx.ELSE() else end_label
        self.ir.add_instruction('if_false_goto', cond_addr, result=target_label)

        # 4. Visitar el bloque THEN
        self.table.enter_scope()
        for statement_ctx in ctx.block(0).statement(): # Iterar sobre los statements del bloque
            self.visit(statement_ctx)
        self.table.exit_scope()

        # 5. Si hay un bloque ELSE, generar salto al final y la etiqueta del ELSE
        if ctx.ELSE():
            self.ir.add_instruction('goto', result=end_label)
            self.ir.add_instruction(f"{else_label}:")
            
            self.table.enter_scope()
            for statement_ctx in ctx.block(1).statement(): # Iterar sobre los statements del bloque ELSE
                self.visit(statement_ctx)
            self.table.exit_scope()

        # 6. Generar la etiqueta final
        self.ir.add_instruction(f"{end_label}:")
        return None
        
    def visitNumberExpr(self, ctx:IfElseLangParser.NumberExprContext):
        return ('int', ctx.NUMBER().getText()) # Devuelve (tipo, valor_literal)

    def visitStringExpr(self, ctx:IfElseLangParser.StringExprContext):
        return ('string', ctx.STRING().getText()) # Devuelve (tipo, valor_literal)

    def visitComparisonExpr(self, ctx:IfElseLangParser.ComparisonExprContext):
        left_type, left_addr = self.visit(ctx.expr(0))
        right_type, right_addr = self.visit(ctx.expr(1))

        if left_type == 'error_type' or right_type == 'error_type':
            return ('error_type', None)

        if left_type != right_type:
            print(f"Error Semántico: Comparación entre tipos incompatibles ({left_type} vs {right_type}).")
            return ('error_type', None)
            
        # Generar IR
        temp = self.ir.new_temp()
        op = ctx.getChild(1).getText() 
        self.ir.add_instruction(op, left_addr, right_addr, temp)
        return ('int', temp)

    def visitArithmeticExpr(self, ctx:IfElseLangParser.ArithmeticExprContext):
        left_type, left_addr = self.visit(ctx.expr(0))
        right_type, right_addr = self.visit(ctx.expr(1))

        if left_type == 'error_type' or right_type == 'error_type':
            return ('error_type', None)

        op = ctx.getChild(1).getText() 

        # Permitir int + int, int - int, etc.
        if left_type == 'int' and right_type == 'int':
            temp = self.ir.new_temp()
            self.ir.add_instruction(op, left_addr, right_addr, temp)
            return ('int', temp)
        
        # Permitir string + string (concatenación)
        if left_type == 'string' and right_type == 'string' and op == '+':
            temp = self.ir.new_temp()
            self.ir.add_instruction(op, left_addr, right_addr, temp)
            return ('string', temp)

        # Cualquier otra combinación es un error.
        print(f"Error Semántico: El operador '{op}' no se puede aplicar a los tipos '{left_type}' y '{right_type}'.")
        return ('error_type', None)

    def visitParenExpr(self, ctx:IfElseLangParser.ParenExprContext):
        return self.visit(ctx.expr()) # Simplemente propaga el tipo y la dirección del resultado