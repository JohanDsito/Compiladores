# Generated from Saludo2.g4 by ANTLR 4.13.1
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
        4,1,4,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,1,1,
        0,1,2,7,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,3,0,0,6,1,1,0,
        0,0,7,8,7,0,0,0,8,3,1,0,0,0,0
    ]

class Saludo2Parser ( Parser ):

    grammarFileName = "Saludo2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hola'", "'buenosdias'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NOMBRE", "WS" ]

    RULE_saludo = 0
    RULE_saludoTipo = 1

    ruleNames =  [ "saludo", "saludoTipo" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NOMBRE=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SaludoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def saludoTipo(self):
            return self.getTypedRuleContext(Saludo2Parser.SaludoTipoContext,0)


        def NOMBRE(self):
            return self.getToken(Saludo2Parser.NOMBRE, 0)

        def getRuleIndex(self):
            return Saludo2Parser.RULE_saludo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludo" ):
                listener.enterSaludo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludo" ):
                listener.exitSaludo(self)




    def saludo(self):

        localctx = Saludo2Parser.SaludoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_saludo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.saludoTipo()
            self.state = 5
            self.match(Saludo2Parser.NOMBRE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaludoTipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Saludo2Parser.RULE_saludoTipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludoTipo" ):
                listener.enterSaludoTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludoTipo" ):
                listener.exitSaludoTipo(self)




    def saludoTipo(self):

        localctx = Saludo2Parser.SaludoTipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_saludoTipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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





