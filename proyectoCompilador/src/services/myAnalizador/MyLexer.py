from antlr4 import *
from services.myantlr4.JavaLexer import JavaLexer
def MyLexer(filePath:str)->str:
    input_stream = FileStream(filePath)
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
    return tokenOut