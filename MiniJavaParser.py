# Generated from MiniJava.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\16\f\4\2\t\2\3\2\3\2\7\2\7\n\2\f\2\16\2\n\13\2\3\2\2")
        buf.write(u"\2\3\2\2\2\2\13\2\4\3\2\2\2\4\b\7\3\2\2\5\7\7\4\2\2\6")
        buf.write(u"\5\3\2\2\2\7\n\3\2\2\2\b\6\3\2\2\2\b\t\3\2\2\2\t\3\3")
        buf.write(u"\2\2\2\n\b\3\2\2\2\3\b")
        return buf.getvalue()


class MiniJavaParser ( Parser ):

    grammarFileName = "MiniJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ u"<INVALID>", u"MainClass", u"ClassDeclaration", u"VarDeclaration", 
                      u"MethodDeclaration", u"Type", u"Statement", u"Experession", 
                      u"Temp", u"Digit", u"LiteralInteger", u"Letter", u"Identifier" ]

    RULE_goal = 0

    ruleNames =  [ u"goal" ]

    EOF = Token.EOF
    MainClass=1
    ClassDeclaration=2
    VarDeclaration=3
    MethodDeclaration=4
    Type=5
    Statement=6
    Experession=7
    Temp=8
    Digit=9
    LiteralInteger=10
    Letter=11
    Identifier=12

    def __init__(self, input, output=sys.stdout):
        super(MiniJavaParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class GoalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MiniJavaParser.GoalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MainClass(self):
            return self.getToken(MiniJavaParser.MainClass, 0)

        def ClassDeclaration(self, i=None):
            if i is None:
                return self.getTokens(MiniJavaParser.ClassDeclaration)
            else:
                return self.getToken(MiniJavaParser.ClassDeclaration, i)

        def getRuleIndex(self):
            return MiniJavaParser.RULE_goal

        def enterRule(self, listener):
            if hasattr(listener, "enterGoal"):
                listener.enterGoal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGoal"):
                listener.exitGoal(self)




    def goal(self):

        localctx = MiniJavaParser.GoalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_goal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MiniJavaParser.MainClass)
            self.state = 6
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniJavaParser.ClassDeclaration:
                self.state = 3
                self.match(MiniJavaParser.ClassDeclaration)
                self.state = 8
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





