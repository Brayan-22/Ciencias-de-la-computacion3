from MyJavaLexer import MyJavaLexer
from MyJavaParser import MyJavaParser
from antlr4 import *

def prueba(filePath:str)->str:
    input_stream = FileStream(filePath)
    lexer = MyJavaLexer(input_stream)
    
    tokenStream = CommonTokenStream(lexer)
    tokenStream.fill()
    tokenTypes = lexer.symbolicNames
    analisis = []
    parser = MyJavaParser(tokenStream)
    if parser.getNumberOfSyntaxErrors() > 0:
        return ("Error de sintaxis")
    else:
        tree = parser.compilationUnit()
        print(tree.toStringTree(recog=parser))
    tokenOut = ""
    for token in tokenStream.tokens:
        temp = f"{tokenTypes[token.type]}:\t --> \t{token.text}"
        analisis.append(str(temp)+"\n")
    tokenOut = tokenOut.join(analisis)
    return tokenOut

salida = prueba("src/resources/input.java")
print(salida)