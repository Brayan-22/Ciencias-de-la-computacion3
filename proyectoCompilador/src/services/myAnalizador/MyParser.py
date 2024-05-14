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
    
    if parser.getNumberOfSyntaxErrors() > 0:
        return ("Error de sintaxis ".join(error.getErrores())) 
    else:
        # linterp = MyListener()
        # walker = ParseTreeWalker()
        # walker.walk(linterp,tree)
        visitor = MyVisitor()
        visitor.visit(tree=tree)
        out = ""
        out = out.join(visitor.analisiSintactico)
        return out