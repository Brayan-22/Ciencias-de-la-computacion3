from antlr4 import *
from services.myantlr4.MyJavaLexer import MyJavaLexer as JavaLexer
from services.myantlr4.MyJavaParser import MyJavaParser as JavaParser
from services.myAnalizador.MyVisitor import VisitorInterp as MyVisitor
from services.myAnalizador.MyErrorListener import MyErrorListener
from services.myAnalizador.MyVisitor import SemanticErrorException
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
    visitor.analisiSintactico = []
    if parser.getNumberOfSyntaxErrors() > 0:
        return ("Error de sintaxis ".join(error.getErrores())) 
    else:
        # linterp = MyListener()
        # walker = ParseTreeWalker()
        # walker.walk(linterp,tree)
        out = ""
        try:
            visitor.visit(tree=tree)
            out = out.join(visitor.analisiSintactico)
        except SemanticErrorException as e:
            out=e
        
        
        return out
