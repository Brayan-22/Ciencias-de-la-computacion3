from antlr4 import *
from services.myantlr4.JavaLexer import JavaLexer
from services.myantlr4.JavaParser import JavaParser
from services.myAnalizador.MyVisitor import VisitorInterp as MyVisitor
from services.myAnalizador.MyErrorListener import MyErrorListener

def MyParser(filePath:str)->str:
    input_stream = FileStream(filePath)
    lexer = JavaLexer(input_stream)
    # Obtener todos los tokens
    tokenStream = CommonTokenStream(lexer)
    parser = JavaParser(tokenStream)
    parser.removeErrorListeners()
    error = MyErrorListener()
    parser.addErrorListener(error)
    tree = parser.compilationUnit()


    
class MyParser():
    def __init__(self) -> None:
        self.input_stream 
        self.lexer
        # Obtener todos los tokens
        self.tokenStream 
        self.parser 
        self.error 
        self.tree 
        self.visitor 
    
    def getSintaxis(self,filePath)->str:
        self.input_stream = FileStream(filePath)
        self.lexer = JavaLexer(self.input_stream)
        # Obtener todos los tokens
        self.tokenStream = CommonTokenStream(self.lexer)
        self.parser = JavaParser(self.tokenStream)
        self.parser.removeErrorListeners()
        self.error = MyErrorListener()
        self.parser.addErrorListener(self.error)
        self.tree = self.parser.compilationUnit()
        self.visitor = MyVisitor()
        if self.parser.getNumberOfSyntaxErrors() > 0:
            return ("Error de sintaxis ".join(self.error.getErrores())) 
        else:
            # linterp = MyListener()
            # walker = ParseTreeWalker()
            # walker.walk(linterp,tree)
            self.visitor.visit(tree=self.tree)
            out = ""
            out = out.join(self.visitor.analisiSintactico)
            return out
        
    def getFields(self)->dict:
        return self.visitor.fields