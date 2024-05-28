import view.vista_principal as v
import flet as ft
# from services.myAnalizador.ResultGen import MyParser as MyParser

# from services.myAnalizador.ResultGen import visitor as visitor
# from antlr4 import *
# from services.myantlr4.MyJavaLexer import MyJavaLexer as JavaLexer
# from services.myantlr4.MyJavaParser import MyJavaParser as JavaParser
# from MyListener import MyListener
def main():
    
    # result = MyParser("src/resources/Inicio.java")
    # print(visitor.tableSimb)
    

    ft.app(v.vista)
    # input_stream = FileStream("src/prueba.txt")
    # lexer = JavaLexer(input_stream)
    # token_stream = CommonTokenStream(lexer)
    # token_stream.fill()
    # parser = JavaParser(token_stream)
    # tree = parser.compilationUnit()
    
    # if parser.getNumberOfSyntaxErrors()>0:
    #     print("Error de sintaxis")
    # else:
    #     tokenTypes = lexer.symbolicNames
    #     for token in token_stream.tokens:
    #         print(f"{tokenTypes[token.type]}: \t --> \t{token.text}")
    #     linterp =MyListener()
    #     walker = ParseTreeWalker()
    #     walker.walk(linterp,tree)
    


if __name__ == "__main__":
    main()