import ply.lex as lex

tokens = (
    "IDENTIFICADOR",
    "NUMERO_ENTERO",
    "NUMERO_DECIMAL",
    "CADENA",
    "CARACTER",
    "OPERADOR_SUMA",
    "OPERADOR_RESTA",
    "OPERADOR_MULTIPLICACION",
    "OPERADOR_DIVISION",
    "PARENTESIS_IZQUIERDO",
    "PARENTESIS_DERECHO",
    "LLAVE_IZQUIERDA",
    "LLAVE_DERECHA",
    "PUNTO_COMA",
    "COMA",
    "PUNTO",
    "ASIGNACION",
    "MAYOR_QUE",
    "MENOR_QUE",
    "IGUALDAD",
    "MAYOR_O_IGUAL_QUE",
    "MENOR_O_IGUAL_QUE",
    "DIFERENTE_DE",
    "AND",
    "OR",
    "NOT",
    "IF",
    "ELSE",
    "WHILE",
    "FOR",
    "TRUE",
    "FALSE",
    "CLASS",
    "PUBLIC",
    "STATIC",
    "VOID",
    "RETURN",
    "CORCHETE_IZQUIERDO",
    "CORCHETE_DERECHO",
)

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMERO_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERO_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

def t_CARACTER(t):
    r'\'(.|\n)\''
    t.value = t.value[1:-1]
    return t

def t_OPERADOR_SUMA(t):
    r'\+\s+'
    return t

def t_OPERADOR_RESTA(t):
    r'-'
    return t

def t_OPERADOR_MULTIPLICACION(t):
    r'\*'
    return t

def t_OPERADOR_DIVISION(t):
    r'/'
    return t

def t_OPERADOR_LOGICO_AND(t):
    r'\&\&'
    return t

def t_OPERADOR_LOGICO_OR(t):
    r'\|\|'
    return t

def t_OPERADOR_LOGICO_NOT(t):
    r'\!'
    return t

def t_PARENTESIS_IZQUIERDO(t):
    r'\('
    return t

def t_PARENTESIS_DERECHO(t):
    r'\)'
    return t

def t_LLAVE_IZQUIERDA(t):
    r'\{'
    return t

def t_LLAVE_DERECHA(t):
    r'\}'
    return t

def t_PUNTO_COMA(t):
    r'\;'
    return t

def t_COMA(t):
    r'\,'
    return t

def t_PUNTO(t):
    r'\.'
    return t

def t_ASIGNACION(t):
    r'\='
    return t

def t_MAYOR_QUE(t):
    r'\>'
    return t

def t_MENOR_QUE(t):
    r'\<'
    return t

def t_IGUALDAD(t):
    r'\=='
    return t

def t_MAYOR_O_IGUAL_QUE(t):
    r'\>='
    return t

def t_MENOR_O_IGUAL_QUE(t):
    r'\<='
    return t

def t_DIFERENTE_DE(t):
    r'\!='
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_VOID(t):
    r'void'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_CORCHETE_IZQUIERDO(t):
    r'\['
    return t

def t_CORCHETE_DERECHO(t):
    r'\]'
    return t

t_ignore = ' \t\n\[\]'

def t_COMENTARIO(t):
    r'//.*\n'
    pass

def t_error(t):
    print("Error: caracter desconocido '%s'" % t.value[0])
    t.lexer.skip(1)

Programa = """
public class HolaMundo {
    private int numero = 5;
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        System.out.println(num);      
        System.out.println("Hola mundo!");

    }
}
"""

lexer = lex.lex()

lexer.input(Programa)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
