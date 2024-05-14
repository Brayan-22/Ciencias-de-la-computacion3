import sys
from antlr4 import *
import json
from myantlr4.JavaLexer import JavaLexer
from myantlr4.JavaParser import JavaParser
from MyVisitor import VisitorInterp as MyVisitor
from MyListener import ListenerInterp as MyListener
from MyErrorListener import MyErrorListener
def main(argv):
    input_stream = FileStream("src/input.java")
    lexer = JavaLexer(input_stream)
    # Obtener todos los tokens
    tokenStream = CommonTokenStream(lexer)
    tokenStream.fill()
    tokenTypes = lexer.symbolicNames
    analisis = []
    tokenOut = ""
    for token in tokenStream.tokens:
        temp = f"{tokenTypes[token.type]}:\t --> \t{token.text}"
        analisis.append(str(temp)+"\n")
    tokenOut = tokenOut.join(analisis)
    print(tokenOut)
    parser = JavaParser(tokenStream)
    parser.removeErrorListeners()
    error = MyErrorListener()
    parser.addErrorListener(error)
    tree = parser.compilationUnit()
    
    # parser.addErrorListener(MyErrorListener)
    # print(tree.toStringTree(recog=parser))
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Error de sintaxis") 
        print(error.getErrores())
    else:
        # linterp = MyListener()
        # walker = ParseTreeWalker()
        # walker.walk(linterp,tree)
        visitor = MyVisitor()
        visitor.visit(tree=tree)
        out = ""
        out = out.join(visitor.analisiSintactico)
        print(out)
    # print(visitor.getVariables())
    print(tree.toStringTree(recog=parser))
    # print(visitor.fields)
    # print(json.dumps(visitor.fields, indent=4))
    # for token in tokenStream.tokens:
    #     print(token)
    # for type in lexer.symbolicNames:
    #     print(type)
    # # Imprimir todos los tokens
    # for token in tokenStream.tokens:
    #     print(token.type)
    # parser = ArrayIntParser(tokenStream)
    # tree = parser.init()
    # print(tree.toStringTree(ruleNames=parser.ruleNames()))


if __name__ == '__main__':
    main(sys.argv)