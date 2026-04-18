import sys
import os

# Agregar la carpeta 'generated' al path para importar el parser
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'generated'))

from WhileLangParser import WhileLangParser
from WhileLangVisitor import WhileLangVisitor
from semantic_analyzer.SymbolTable import SymbolTable


class SemanticVisitor(WhileLangVisitor):
    """
    Visitor semantico para WhileLang.
    Realiza verificacion de tipos y manejo de ambitos (scopes).
    """

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.loop_depth = 0  # Profundidad de bucles para validar break/continue

    def _error(self, message):
        """Registra e imprime un error semantico."""
        print(f"Error Semantico: {message}")
        self.errors.append(message)

    # -------------------------------------------------------------------------
    # Programa y declaraciones
    # -------------------------------------------------------------------------

    def visitProgram(self, ctx: WhileLangParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitDeclStatement(self, ctx: WhileLangParser.DeclStatementContext):
        return self.visit(ctx.declaration())

    def visitDeclaration(self, ctx: WhileLangParser.DeclarationContext):
        var_type = ctx.type_().getText()   # 'int' o 'string'
        var_name = ctx.ID().getText()
        expr_type = self.visit(ctx.expr())

        if expr_type == 'error_type':
            # Error ya reportado mas abajo; registrar el simbolo de todas formas
            self.symbol_table.declare(var_name, var_type)
            return None

        # Verificar compatibilidad de tipos
        if expr_type != var_type:
            self._error(
                f"Tipo incompatible: no se puede asignar '{expr_type}' a variable "
                f"de tipo '{var_type}' ('{var_name}')."
            )
            self.symbol_table.declare(var_name, var_type)
            return None

        # Registrar en la tabla de simbolos
        if not self.symbol_table.declare(var_name, var_type):
            self._error(f"Redeclaracion: la variable '{var_name}' ya fue declarada en este ambito.")

        return None

    def visitAssignStatement(self, ctx: WhileLangParser.AssignStatementContext):
        return self.visit(ctx.assignment())

    def visitAssignment(self, ctx: WhileLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        declared_type = self.symbol_table.lookup(var_name)

        if declared_type is None:
            self._error(f"Variable no declarada: '{var_name}'.")
            self.visit(ctx.expr())
            return None

        expr_type = self.visit(ctx.expr())

        if expr_type != 'error_type' and expr_type != declared_type:
            self._error(
                f"Tipo incompatible: no se puede asignar '{expr_type}' "
                f"a '{var_name}' de tipo '{declared_type}'."
            )

        return None

    # -------------------------------------------------------------------------
    # Estructuras de control
    # -------------------------------------------------------------------------

    def visitWhileStmt(self, ctx: WhileLangParser.WhileStmtContext):
        return self.visit(ctx.whileStatement())

    def visitWhileStatement(self, ctx: WhileLangParser.WhileStatementContext):
        cond_type = self.visit(ctx.condition())
        if cond_type == 'error_type':
            pass  # Error ya reportado

        self.symbol_table.enter_scope()
        self.loop_depth += 1
        for stmt in ctx.statement():
            self.visit(stmt)
        self.loop_depth -= 1
        self.symbol_table.exit_scope()
        return None

    def visitIfStmt(self, ctx: WhileLangParser.IfStmtContext):
        return self.visit(ctx.ifStatement())

    def visitIfStatement(self, ctx: WhileLangParser.IfStatementContext):
        cond_type = self.visit(ctx.condition())
        if cond_type == 'error_type':
            pass  # Error ya reportado

        # Rama 'then'
        self.symbol_table.enter_scope()
        stmts = ctx.statement()
        # Identificar los statement del bloque then (antes del else, si existe)
        lbrace_count = 0
        in_then = True
        for child in ctx.getChildren():
            text = child.getText() if hasattr(child, 'getText') else ''
            if text == '{':
                lbrace_count += 1
            if text == '}' and lbrace_count == 1:
                in_then = False

        # Visitamos usando los indices de ctx.statement()
        # La gramatica garantiza que los primeros stmt son del then y los demas del else
        has_else = ctx.ELSE() is not None
        if has_else:
            # Contar llaves para separar bloques then/else
            # Usamos una heuristica: visitamos todos los statements del then scope
            # Accedemos por indice: los del then son los que estan antes del ELSE token
            then_stmts = []
            else_stmts = []
            found_else = False
            for child in ctx.children:
                token_text = child.getText() if hasattr(child, 'getText') else ''
                if token_text == 'else':
                    found_else = True
                    continue
                if hasattr(child, 'statement'):
                    pass
            # Approach mas simple: usar ctx.statement() directamente
            # ANTLR agrupa todos los statement() en una sola lista
            # Necesitamos contar cuantos hay en el then vs else
            # Lo hacemos contando las llaves del bloque then
            all_stmts = ctx.statement()
            # Contamos statements en el then buscando la posicion del ELSE
            n_then = 0
            brace_depth = 0
            for child in ctx.children:
                text = child.getText() if hasattr(child, 'getText') else ''
                if text == 'else':
                    break
                if text == '{':
                    brace_depth += 1
                elif text == '}':
                    brace_depth -= 1
                elif hasattr(child, 'statement') or child.__class__.__name__ == 'StatementContext':
                    n_then += 1

            then_stmts = all_stmts[:n_then]
            else_stmts = all_stmts[n_then:]

            for stmt in then_stmts:
                self.visit(stmt)
            self.symbol_table.exit_scope()

            self.symbol_table.enter_scope()
            for stmt in else_stmts:
                self.visit(stmt)
            self.symbol_table.exit_scope()
        else:
            for stmt in stmts:
                self.visit(stmt)
            self.symbol_table.exit_scope()

        return None

    def visitBreakStmt(self, ctx: WhileLangParser.BreakStmtContext):
        if self.loop_depth == 0:
            self._error("'break' fuera de un bucle.")
        return None

    def visitContinueStmt(self, ctx: WhileLangParser.ContinueStmtContext):
        if self.loop_depth == 0:
            self._error("'continue' fuera de un bucle.")
        return None

    # -------------------------------------------------------------------------
    # Condiciones
    # -------------------------------------------------------------------------

    def visitExprCondition(self, ctx: WhileLangParser.ExprConditionContext):
        """Condicion que es solo una expresion (p.ej., if (s))."""
        expr_type = self.visit(ctx.expr())
        if expr_type != 'error_type' and expr_type != 'int':
            self._error(
                f"Condicion invalida: se esperaba tipo 'int', pero se encontro '{expr_type}'. "
                f"Las condiciones solo pueden ser enteros o comparaciones."
            )
            return 'error_type'
        return 'int'

    def visitComparisonCondition(self, ctx: WhileLangParser.ComparisonConditionContext):
        """Condicion de comparacion: expr op expr."""
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        if left_type != right_type:
            self._error(
                f"Comparacion entre tipos incompatibles ('{left_type}' vs '{right_type}')."
            )
            return 'error_type'

        # Solo se permiten comparaciones entre enteros
        if left_type != 'int':
            self._error(
                f"Comparaciones solo permitidas entre enteros, no entre '{left_type}'."
            )
            return 'error_type'

        return 'int'

    # -------------------------------------------------------------------------
    # Expresiones
    # -------------------------------------------------------------------------

    def visitIdExpr(self, ctx: WhileLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        var_type = self.symbol_table.lookup(var_name)
        if var_type is None:
            self._error(f"Variable no declarada: '{var_name}'.")
            return 'error_type'
        return var_type

    def visitNumberExpr(self, ctx: WhileLangParser.NumberExprContext):
        return 'int'

    def visitStringExpr(self, ctx: WhileLangParser.StringExprContext):
        return 'string'

    def visitParenExpr(self, ctx: WhileLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitArithmeticExpr(self, ctx: WhileLangParser.ArithmeticExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        op = ctx.getChild(1).getText()

        # Concatenacion de strings solo con '+'
        if left_type == 'string' and right_type == 'string':
            if op == '+':
                return 'string'
            else:
                self._error(
                    f"Operacion '{op}' no permitida entre strings. "
                    f"Solo se permite '+' para concatenacion."
                )
                return 'error_type'

        # Operaciones aritmeticas solo entre enteros
        if left_type == 'int' and right_type == 'int':
            return 'int'

        # Tipos mezclados
        self._error(
            f"Operacion '{op}' entre tipos incompatibles ('{left_type}' y '{right_type}')."
        )
        return 'error_type'
