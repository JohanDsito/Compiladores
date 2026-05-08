# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#DronDecl.
    def enterDronDecl(self, ctx:gramaticaParser.DronDeclContext):
        pass

    # Exit a parse tree produced by gramaticaParser#DronDecl.
    def exitDronDecl(self, ctx:gramaticaParser.DronDeclContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ZonaDecl.
    def enterZonaDecl(self, ctx:gramaticaParser.ZonaDeclContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ZonaDecl.
    def exitZonaDecl(self, ctx:gramaticaParser.ZonaDeclContext):
        pass


    # Enter a parse tree produced by gramaticaParser#mission.
    def enterMission(self, ctx:gramaticaParser.MissionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#mission.
    def exitMission(self, ctx:gramaticaParser.MissionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#command.
    def enterCommand(self, ctx:gramaticaParser.CommandContext):
        pass

    # Exit a parse tree produced by gramaticaParser#command.
    def exitCommand(self, ctx:gramaticaParser.CommandContext):
        pass


    # Enter a parse tree produced by gramaticaParser#SimpleAction.
    def enterSimpleAction(self, ctx:gramaticaParser.SimpleActionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#SimpleAction.
    def exitSimpleAction(self, ctx:gramaticaParser.SimpleActionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#MoverAction.
    def enterMoverAction(self, ctx:gramaticaParser.MoverActionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#MoverAction.
    def exitMoverAction(self, ctx:gramaticaParser.MoverActionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#IrAAction.
    def enterIrAAction(self, ctx:gramaticaParser.IrAActionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#IrAAction.
    def exitIrAAction(self, ctx:gramaticaParser.IrAActionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#GirarAction.
    def enterGirarAction(self, ctx:gramaticaParser.GirarActionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#GirarAction.
    def exitGirarAction(self, ctx:gramaticaParser.GirarActionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#direction.
    def enterDirection(self, ctx:gramaticaParser.DirectionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#direction.
    def exitDirection(self, ctx:gramaticaParser.DirectionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#SiControl.
    def enterSiControl(self, ctx:gramaticaParser.SiControlContext):
        pass

    # Exit a parse tree produced by gramaticaParser#SiControl.
    def exitSiControl(self, ctx:gramaticaParser.SiControlContext):
        pass


    # Enter a parse tree produced by gramaticaParser#RepetirControl.
    def enterRepetirControl(self, ctx:gramaticaParser.RepetirControlContext):
        pass

    # Exit a parse tree produced by gramaticaParser#RepetirControl.
    def exitRepetirControl(self, ctx:gramaticaParser.RepetirControlContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condition.
    def enterCondition(self, ctx:gramaticaParser.ConditionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condition.
    def exitCondition(self, ctx:gramaticaParser.ConditionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#sensor.
    def enterSensor(self, ctx:gramaticaParser.SensorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#sensor.
    def exitSensor(self, ctx:gramaticaParser.SensorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#comparator.
    def enterComparator(self, ctx:gramaticaParser.ComparatorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#comparator.
    def exitComparator(self, ctx:gramaticaParser.ComparatorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#waitCmd.
    def enterWaitCmd(self, ctx:gramaticaParser.WaitCmdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#waitCmd.
    def exitWaitCmd(self, ctx:gramaticaParser.WaitCmdContext):
        pass



del gramaticaParser