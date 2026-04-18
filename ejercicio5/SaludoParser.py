# Generated from Saludo.g4 by ANTLR 4.13.1
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
        4,1,3,6,2,0,7,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,4,0,2,1,0,0,0,2,3,5,
        1,0,0,3,4,5,2,0,0,4,1,1,0,0,0,0
    ]

class SaludoParser ( Parser ):

    grammarFileName = "Saludo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hola'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NOMBRE", "WS" ]

    RULE_saludo = 0

    ruleNames =  [ "saludo" ]

    EOF = Token.EOF
    T__0=1
    NOMBRE=2
    WS=3

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

        def NOMBRE(self):
            return self.getToken(SaludoParser.NOMBRE, 0)

        def getRuleIndex(self):
            return SaludoParser.RULE_saludo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludo" ):
                listener.enterSaludo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludo" ):
                listener.exitSaludo(self)




    def saludo(self):

        localctx = SaludoParser.SaludoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_saludo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(SaludoParser.T__0)
            self.state = 3
            self.match(SaludoParser.NOMBRE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





