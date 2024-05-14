import sys
from antlr4 import *

from myantlr4.javaAntlr4.MyJavaLexer import MyJavaLexer as JavaLexer
from myantlr4.javaAntlr4.MyJavaParser import MyJavaParser as JavaParser
# from MyVisitor import VisitorInterp
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JavaLexer(input_stream)
    # Obtener todos los tokens
    tokenStream = CommonTokenStream(lexer)
    tokenStream.fill()
    tokenTypes = lexer.symbolicNames
    analisis = []
    tokenOut = ""
    for token in tokenStream.tokens:
        # temp = f"{tokenTypes[token.type]}:\t->{token.text}"
        temp = str(token)
        analisis.append(str(temp)+"\n")
        #print(temp)
    tokenOut = tokenOut.join(analisis)
    print("ANALIZADOR LEXICO: ")
    print(tokenOut)
    print("------------------")
    print("ANALIZADOR SINTACTICO:")
    # parser = JavaParser(tokenStream)
    # if parser.getNumberOfSyntaxErrors() > 0:
    #     print("syntax errors")
    # else:
    #     tree = parser.compilationUnit()
    #     vinterp = VisitorInterp()
    #     vinterp.visit(tree)

    
    # parser = JavaParser(tokenStream)
    # tree = parser.compilationUnit()
    # print(tree.toStringTree(recog=parser))
    
    
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