# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#program.
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#DronDecl.
    def visitDronDecl(self, ctx:gramaticaParser.DronDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ZonaDecl.
    def visitZonaDecl(self, ctx:gramaticaParser.ZonaDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#mission.
    def visitMission(self, ctx:gramaticaParser.MissionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#command.
    def visitCommand(self, ctx:gramaticaParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#SimpleAction.
    def visitSimpleAction(self, ctx:gramaticaParser.SimpleActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#MoverAction.
    def visitMoverAction(self, ctx:gramaticaParser.MoverActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#IrAAction.
    def visitIrAAction(self, ctx:gramaticaParser.IrAActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#GirarAction.
    def visitGirarAction(self, ctx:gramaticaParser.GirarActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#direction.
    def visitDirection(self, ctx:gramaticaParser.DirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#SiControl.
    def visitSiControl(self, ctx:gramaticaParser.SiControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#RepetirControl.
    def visitRepetirControl(self, ctx:gramaticaParser.RepetirControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condition.
    def visitCondition(self, ctx:gramaticaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#sensor.
    def visitSensor(self, ctx:gramaticaParser.SensorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#comparator.
    def visitComparator(self, ctx:gramaticaParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#waitCmd.
    def visitWaitCmd(self, ctx:gramaticaParser.WaitCmdContext):
        return self.visitChildren(ctx)



del gramaticaParser