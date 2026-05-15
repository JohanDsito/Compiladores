# Generated from gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,4,0,26,8,0,11,0,
        12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        43,8,1,1,2,1,2,1,2,1,2,4,2,49,8,2,11,2,12,2,50,1,2,1,2,1,3,1,3,1,
        3,3,3,58,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,78,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,89,8,6,1,6,1,6,1,6,1,6,1,6,4,6,96,8,6,11,6,12,6,97,1,6,1,6,
        3,6,102,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,5,1,0,10,
        12,1,0,16,17,1,0,16,21,1,0,28,30,1,0,31,35,120,0,25,1,0,0,0,2,42,
        1,0,0,0,4,44,1,0,0,0,6,57,1,0,0,0,8,77,1,0,0,0,10,79,1,0,0,0,12,
        101,1,0,0,0,14,103,1,0,0,0,16,109,1,0,0,0,18,111,1,0,0,0,20,113,
        1,0,0,0,22,26,3,2,1,0,23,26,3,4,2,0,24,26,3,6,3,0,25,22,1,0,0,0,
        25,23,1,0,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,
        0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,32,5,1,0,0,32,
        33,5,38,0,0,33,43,5,2,0,0,34,35,5,3,0,0,35,36,5,38,0,0,36,37,5,4,
        0,0,37,38,5,39,0,0,38,39,5,5,0,0,39,40,5,39,0,0,40,41,5,6,0,0,41,
        43,5,2,0,0,42,31,1,0,0,0,42,34,1,0,0,0,43,3,1,0,0,0,44,45,5,7,0,
        0,45,46,5,38,0,0,46,48,5,8,0,0,47,49,3,6,3,0,48,47,1,0,0,0,49,50,
        1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,5,9,0,0,
        53,5,1,0,0,0,54,58,3,8,4,0,55,58,3,12,6,0,56,58,3,20,10,0,57,54,
        1,0,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,7,1,0,0,0,59,60,7,0,0,0,60,
        61,5,38,0,0,61,78,5,2,0,0,62,63,5,13,0,0,63,64,5,38,0,0,64,65,3,
        10,5,0,65,66,5,39,0,0,66,67,5,2,0,0,67,78,1,0,0,0,68,69,5,14,0,0,
        69,70,5,38,0,0,70,71,5,38,0,0,71,78,5,2,0,0,72,73,5,15,0,0,73,74,
        5,38,0,0,74,75,7,1,0,0,75,76,5,39,0,0,76,78,5,2,0,0,77,59,1,0,0,
        0,77,62,1,0,0,0,77,68,1,0,0,0,77,72,1,0,0,0,78,9,1,0,0,0,79,80,7,
        2,0,0,80,11,1,0,0,0,81,82,5,22,0,0,82,83,3,14,7,0,83,84,5,23,0,0,
        84,88,3,6,3,0,85,86,5,24,0,0,86,87,5,23,0,0,87,89,3,6,3,0,88,85,
        1,0,0,0,88,89,1,0,0,0,89,102,1,0,0,0,90,91,5,25,0,0,91,92,5,39,0,
        0,92,93,5,26,0,0,93,95,5,8,0,0,94,96,3,6,3,0,95,94,1,0,0,0,96,97,
        1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,9,0,0,
        100,102,1,0,0,0,101,81,1,0,0,0,101,90,1,0,0,0,102,13,1,0,0,0,103,
        104,5,38,0,0,104,105,5,27,0,0,105,106,3,16,8,0,106,107,3,18,9,0,
        107,108,5,39,0,0,108,15,1,0,0,0,109,110,7,3,0,0,110,17,1,0,0,0,111,
        112,7,4,0,0,112,19,1,0,0,0,113,114,5,36,0,0,114,115,5,39,0,0,115,
        116,5,37,0,0,116,117,5,2,0,0,117,21,1,0,0,0,9,25,27,42,50,57,77,
        88,97,101
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'drone'", "';'", "'zona'", "'('", "','", 
                     "')'", "'mision'", "'{'", "'}'", "'despegar'", "'aterrizar'", 
                     "'hover'", "'mover'", "'ir_a'", "'girar'", "'izquierda'", 
                     "'derecha'", "'adelante'", "'atras'", "'arriba'", "'abajo'", 
                     "'si'", "':'", "'sino'", "'repetir'", "'veces'", "'.'", 
                     "'altitud'", "'bateria'", "'distancia'", "'<'", "'>'", 
                     "'=='", "'<='", "'>='", "'esperar'", "'s'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "COMMENT", 
                      "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_mission = 2
    RULE_command = 3
    RULE_action = 4
    RULE_direction = 5
    RULE_control = 6
    RULE_condition = 7
    RULE_sensor = 8
    RULE_comparator = 9
    RULE_waitCmd = 10

    ruleNames =  [ "program", "declaration", "mission", "command", "action", 
                   "direction", "control", "condition", "sensor", "comparator", 
                   "waitCmd" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    ID=38
    NUMBER=39
    COMMENT=40
    BLOCK_COMMENT=41
    WS=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DeclarationContext,i)


        def mission(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.MissionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.MissionContext,i)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CommandContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CommandContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3]:
                    self.state = 22
                    self.declaration()
                    pass
                elif token in [7]:
                    self.state = 23
                    self.mission()
                    pass
                elif token in [10, 11, 12, 13, 14, 15, 22, 25, 36]:
                    self.state = 24
                    self.command()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 68757290122) != 0)):
                    break

            self.state = 29
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DronDeclContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDronDecl" ):
                listener.enterDronDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDronDecl" ):
                listener.exitDronDecl(self)


    class ZonaDeclContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NUMBER)
            else:
                return self.getToken(gramaticaParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZonaDecl" ):
                listener.enterZonaDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZonaDecl" ):
                listener.exitZonaDecl(self)



    def declaration(self):

        localctx = gramaticaParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = gramaticaParser.DronDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(gramaticaParser.T__0)
                self.state = 32
                self.match(gramaticaParser.ID)
                self.state = 33
                self.match(gramaticaParser.T__1)
                pass
            elif token in [3]:
                localctx = gramaticaParser.ZonaDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(gramaticaParser.T__2)
                self.state = 35
                self.match(gramaticaParser.ID)
                self.state = 36
                self.match(gramaticaParser.T__3)
                self.state = 37
                self.match(gramaticaParser.NUMBER)
                self.state = 38
                self.match(gramaticaParser.T__4)
                self.state = 39
                self.match(gramaticaParser.NUMBER)
                self.state = 40
                self.match(gramaticaParser.T__5)
                self.state = 41
                self.match(gramaticaParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MissionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CommandContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CommandContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_mission

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMission" ):
                listener.enterMission(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMission" ):
                listener.exitMission(self)




    def mission(self):

        localctx = gramaticaParser.MissionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mission)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(gramaticaParser.T__6)
            self.state = 45
            self.match(gramaticaParser.ID)
            self.state = 46
            self.match(gramaticaParser.T__7)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self.command()
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 68757289984) != 0)):
                    break

            self.state = 52
            self.match(gramaticaParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(gramaticaParser.ActionContext,0)


        def control(self):
            return self.getTypedRuleContext(gramaticaParser.ControlContext,0)


        def waitCmd(self):
            return self.getTypedRuleContext(gramaticaParser.WaitCmdContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = gramaticaParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_command)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.action()
                pass
            elif token in [22, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.control()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.waitCmd()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_action

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GirarActionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)
        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGirarAction" ):
                listener.enterGirarAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGirarAction" ):
                listener.exitGirarAction(self)


    class MoverActionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)
        def direction(self):
            return self.getTypedRuleContext(gramaticaParser.DirectionContext,0)

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoverAction" ):
                listener.enterMoverAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoverAction" ):
                listener.exitMoverAction(self)


    class SimpleActionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAction" ):
                listener.enterSimpleAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAction" ):
                listener.exitSimpleAction(self)


    class IrAActionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIrAAction" ):
                listener.enterIrAAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIrAAction" ):
                listener.exitIrAAction(self)



    def action(self):

        localctx = gramaticaParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12]:
                localctx = gramaticaParser.SimpleActionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
                self.match(gramaticaParser.ID)
                self.state = 61
                self.match(gramaticaParser.T__1)
                pass
            elif token in [13]:
                localctx = gramaticaParser.MoverActionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(gramaticaParser.T__12)
                self.state = 63
                self.match(gramaticaParser.ID)
                self.state = 64
                self.direction()
                self.state = 65
                self.match(gramaticaParser.NUMBER)
                self.state = 66
                self.match(gramaticaParser.T__1)
                pass
            elif token in [14]:
                localctx = gramaticaParser.IrAActionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(gramaticaParser.T__13)
                self.state = 69
                self.match(gramaticaParser.ID)
                self.state = 70
                self.match(gramaticaParser.ID)
                self.state = 71
                self.match(gramaticaParser.T__1)
                pass
            elif token in [15]:
                localctx = gramaticaParser.GirarActionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(gramaticaParser.T__14)
                self.state = 73
                self.match(gramaticaParser.ID)
                self.state = 74
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 75
                self.match(gramaticaParser.NUMBER)
                self.state = 76
                self.match(gramaticaParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_direction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirection" ):
                listener.enterDirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirection" ):
                listener.exitDirection(self)




    def direction(self):

        localctx = gramaticaParser.DirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_direction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_control

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepetirControlContext(ControlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ControlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)
        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CommandContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CommandContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetirControl" ):
                listener.enterRepetirControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetirControl" ):
                listener.exitRepetirControl(self)


    class SiControlContext(ControlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ControlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self):
            return self.getTypedRuleContext(gramaticaParser.ConditionContext,0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CommandContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CommandContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSiControl" ):
                listener.enterSiControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSiControl" ):
                listener.exitSiControl(self)



    def control(self):

        localctx = gramaticaParser.ControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_control)
        self._la = 0 # Token type
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = gramaticaParser.SiControlContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(gramaticaParser.T__21)
                self.state = 82
                self.condition()
                self.state = 83
                self.match(gramaticaParser.T__22)
                self.state = 84
                self.command()
                self.state = 88
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 85
                    self.match(gramaticaParser.T__23)
                    self.state = 86
                    self.match(gramaticaParser.T__22)
                    self.state = 87
                    self.command()


                pass
            elif token in [25]:
                localctx = gramaticaParser.RepetirControlContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(gramaticaParser.T__24)
                self.state = 91
                self.match(gramaticaParser.NUMBER)
                self.state = 92
                self.match(gramaticaParser.T__25)
                self.state = 93
                self.match(gramaticaParser.T__7)
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 94
                    self.command()
                    self.state = 97 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 68757289984) != 0)):
                        break

                self.state = 99
                self.match(gramaticaParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def sensor(self):
            return self.getTypedRuleContext(gramaticaParser.SensorContext,0)


        def comparator(self):
            return self.getTypedRuleContext(gramaticaParser.ComparatorContext,0)


        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = gramaticaParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(gramaticaParser.ID)
            self.state = 104
            self.match(gramaticaParser.T__26)
            self.state = 105
            self.sensor()
            self.state = 106
            self.comparator()
            self.state = 107
            self.match(gramaticaParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SensorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_sensor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSensor" ):
                listener.enterSensor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSensor" ):
                listener.exitSensor(self)




    def sensor(self):

        localctx = gramaticaParser.SensorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sensor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = gramaticaParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66571993088) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_waitCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitCmd" ):
                listener.enterWaitCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitCmd" ):
                listener.exitWaitCmd(self)




    def waitCmd(self):

        localctx = gramaticaParser.WaitCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_waitCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(gramaticaParser.T__35)
            self.state = 114
            self.match(gramaticaParser.NUMBER)
            self.state = 115
            self.match(gramaticaParser.T__36)
            self.state = 116
            self.match(gramaticaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





