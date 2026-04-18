# semantic_analyzer/SemanticVisitor.py
from generated.IfElseLangVisitor import IfElseLangVisitor
from generated.IfElseLangParser import IfElseLangParser
from .SymbolTable import SymbolTable, Symbol

class SemanticVisitor(IfElseLangVisitor):
    def __init__(self):
        self.table = SymbolTable()

    # Declaración de variables
    def visitDeclaration(self, ctx:IfElseLangParser.DeclarationContext):
        var_name = ctx.ID().getText()
        type_name = ctx.type_().getText()
        self.table.insert(var_name, Symbol(var_name, type_name))
        return self.visitChildren(ctx)

    # Asignación
    def visitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' a la que se intenta asignar no ha sido declarada.")
            return None

        expr_type = self.visit(ctx.expr())

        if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
            print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a variable '{var_name}' de tipo '{symbol.type}'.")
        return None

    # Expresión: identificador
    def visitIdExpr(self, ctx:IfElseLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)
        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
            return 'error_type'
        return symbol.type

    # Expresión: número
    def visitNumberExpr(self, ctx:IfElseLangParser.NumberExprContext):
        return 'int'

    # Expresión: comparación
    def visitComparisonExpr(self, ctx:IfElseLangParser.ComparisonExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        if left_type != right_type:
            print(f"Error Semántico: Comparación entre tipos incompatibles ({left_type} vs {right_type}).")
            return 'error_type'

        return 'int'  # tratamos el booleano como int simple

    # Expresión: aritmética
    def visitArithmeticExpr(self, ctx:IfElseLangParser.ArithmeticExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        if left_type != 'int' or right_type != 'int':
            print(f"Error Semántico: Operación aritmética solo permitida con enteros, no con {left_type} y {right_type}.")
            return 'error_type'

        return 'int'

    # Expresión: paréntesis
    def visitParenExpr(self, ctx:IfElseLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    # If con scopes separados
    def visitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        # Verificar condición
        self.visit(ctx.condition())

        # Statements dentro del bloque THEN
        self.table.enter_scope()
        for stmt in ctx.statement()[:len(ctx.statement()) // (2 if ctx.ELSE() else 1)]:
            self.visit(stmt)
        self.table.exit_scope()

        # Statements dentro del bloque ELSE
        if ctx.ELSE():
            self.table.enter_scope()
            for stmt in ctx.statement()[len(ctx.statement()) // 2:]:
                self.visit(stmt)
            self.table.exit_scope()

        return None
    def visitStringExpr(self, ctx:IfElseLangParser.StringExprContext):
        return 'string'