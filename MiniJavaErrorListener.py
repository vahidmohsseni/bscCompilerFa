import sys
# from ProjectListener import ProjectListener
from MiniJavaListener import MiniJavaListener
from antlr4.error.ErrorListener import ErrorListener

class LexerErrorListener(ErrorListener):

    def __init__(self):
        super(LexerErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise CompilerException(line=line, column=column, msg=msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print "Ambiguity error : " + str(configs)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print "Attempting full context error : " + str(configs)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print "Context error : " + str(configs)



class ParserErrorListener(ErrorListener):

    def __init__(self):
        super(ParserErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(CompilerException(line, column, msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print "Ambiguity error : " + str(configs)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print "Attempting full context error : " + str(configs)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print "Context error : " + str(configs)


class CompilerException(Exception):
    def __init__(self, line, column, msg):
        super(CompilerException, self).__init__()
        self.line = line
        self.column = column
        self.msg = msg
        self.error_msg = "%s:%s: %s" % (line, column, msg)
        super(SyntaxErrorException, self).__init__(self.error_msg)


class DeclarationException(Exception):
    def __init__(self, identifier):
        super(DeclarationException, self).__init__("'%s' not declared" % identifier)
