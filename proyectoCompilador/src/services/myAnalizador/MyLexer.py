from antlr4 import *
from services.myantlr4.MyJavaLexer import MyJavaLexer as JavaLexer
from services.myAnalizador.MyErrorListener import MyErrorListener

def MyLexer(filePath:str)->str:
    input_stream = FileStream(filePath)
    lexer = JavaLexer(input_stream)
    # Obtener todos los tokens
    tokenStream = CommonTokenStream(lexer)
    tokenStream.fill()
    tokenTypes = lexer.symbolicNames
    analisis = []
    tokenOut = ""
    errores = lexer.getErrors()
    for token in tokenStream.tokens:
        temp = f"{tokenTypes[token.type]}:\t --> \t{token.text}"
        analisis.append(str(temp)+"\n")
    for error in errores:
        analisis.append(error+"\n")
    tokenOut = tokenOut.join(analisis)
    return tokenOut

