# from lexico import lexer
from parse import parser
import ply.lex as lexer
def analizar_codigo(input_text)->str:
    lexer.input(input_text)
    # for token in lexer:
    #     print(token)
    result = parser.parse(input_text)
    return result

Programa = """
public class HolaMundo {
    private int numero = 5;
    public static void main(String[] args) {
        public int a = 0;
        public int b = 5;
        a= a+b;
    }
}
"""
analizar_codigo(Programa)