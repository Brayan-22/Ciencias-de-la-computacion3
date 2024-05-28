from antlr4 import *
from services.myantlr4.MyJavaLexer import MyJavaLexer as JavaLexer
from services.myantlr4.MyJavaParser import MyJavaParser as JavaParser
from services.myAnalizador.VisitorNinfija import MyVistorNinfija as MyVisitor
from services.myAnalizador.MyErrorListener import MyErrorListener
import json


visitor = MyVisitor()
    
def MyParser(filePath:str):
    input_stream = FileStream(filePath)
    lexer = JavaLexer(input_stream)
    # Obtener todos los tokens
    tokenStream = CommonTokenStream(lexer)
    parser = JavaParser(tokenStream)
    parser.removeErrorListeners()
    error = MyErrorListener()
    parser.addErrorListener(error)
    tree = parser.compilationUnit()
    visitor.pila = []
    visitor.temp = 1 
    if parser.getNumberOfSyntaxErrors() > 0:
        return ("Error de sintaxis ".join(error.getErrores())) 
    else:
        # linterp = MyListener()
        # walker = ParseTreeWalker()
        # walker.walk(linterp,tree)
        visitor.visit(tree=tree)
        with open('src/codInterp.txt', 'w') as fichero:
            fichero.writelines(visitor.pila)
