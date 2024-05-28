from antlr4 import *
from services.myantlr4.MyJavaLexer import MyJavaLexer as JavaLexer
from services.myantlr4.MyJavaParser import MyJavaParser as JavaParser
from services.myAnalizador.VisitorNinfija2 import MyVistorNinfija as MyVisitor
from services.myAnalizador.MyErrorListener import MyErrorListener
import json


visitor = MyVisitor()
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
    visitor.tableSimb = {}
    visitor.temp=1
    if parser.getNumberOfSyntaxErrors() > 0:
        return ("Error de sintaxis ".join(error.getErrores())) 
    else:
        # linterp = MyListener()
        # walker = ParseTreeWalker()
        # walker.walk(linterp,tree)
        out = ""
        visitor.visit(tree=tree)
        print(visitor.tableSimb)
        return out;
