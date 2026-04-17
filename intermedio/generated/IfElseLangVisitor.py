# Generated from IfElseLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .IfElseLangParser import IfElseLangParser
else:
    from IfElseLangParser import IfElseLangParser

# This class defines a complete generic visitor for a parse tree produced by IfElseLangParser.

class IfElseLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IfElseLangParser#program.
    def visitProgram(self, ctx:IfElseLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#functionDecl.
    def visitFunctionDecl(self, ctx:IfElseLangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#param.
    def visitParam(self, ctx:IfElseLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#paramList.
    def visitParamList(self, ctx:IfElseLangParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#declaration.
    def visitDeclaration(self, ctx:IfElseLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#type.
    def visitType(self, ctx:IfElseLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#statement.
    def visitStatement(self, ctx:IfElseLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#returnStatement.
    def visitReturnStatement(self, ctx:IfElseLangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#assignment.
    def visitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#ifStatement.
    def visitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#condition.
    def visitCondition(self, ctx:IfElseLangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#stringExpr.
    def visitStringExpr(self, ctx:IfElseLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#numberExpr.
    def visitNumberExpr(self, ctx:IfElseLangParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:IfElseLangParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:IfElseLangParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:IfElseLangParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#parenExpr.
    def visitParenExpr(self, ctx:IfElseLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#idExpr.
    def visitIdExpr(self, ctx:IfElseLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#argList.
    def visitArgList(self, ctx:IfElseLangParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfElseLangParser#block.
    def visitBlock(self, ctx:IfElseLangParser.BlockContext):
        return self.visitChildren(ctx)



del IfElseLangParser