from antlr4.error.ErrorListener import ErrorListener
import sys

class MyErrorListener(ErrorListener):
    def __init__(self):
        self.errores=[]
    # INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append("linea " + str(line) + ":" + str(column) + " " + msg)
        # print("line " + str(line) + ":" + str(column) + " " + msg+"holaaaa", file=sys.stderr)
        

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass
    def getErrores(self)->list[str]:
        return self.errores
