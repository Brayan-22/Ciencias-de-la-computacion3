import ply.lex as lex
tokens = (
    "IDENTIFICADOR",
    "NUMERO_ENTERO",
    "NUMERO_DECIMAL",
    "CARACTER",
    "CADENA",
    "OPERADOR_INCREMENTO",
    "OPERADOR_DECREMENTO",
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
    "MAYOR_IGUAL_QUE",
    "MAYOR_QUE",
    "MENOR_IGUAL_QUE",
    "MENOR_QUE",
    "IGUALDAD",
    "MAYOR_O_IGUAL_QUE",
    "MENOR_O_IGUAL_QUE",
    "DIFERENTE_DE",
    "OPERADOR_LOGICO_AND",
    "OPERADOR_LOGICO_OR",
    "OPERADOR_LOGICO_NOT",
    "CORCHETE_IZQUIERDO",
    "CORCHETE_DERECHO",
    "TIPO_DATO",
    "MOD_ACCESO",
    "MODIFICADOR",
    "TIPO_FUNCION",
    "PALABRA_RESERVADA",
    "DOS_PUNTOS",
    "COMENTARIO",
    "BLOQUE_COMENTARIO"
)

palabrasReservadas = {
    "public": "MOD_ACCESO",
    "static": "MODIFICADOR",
    "in":"PALABRA_RESERVADA",
    "void": "TIPO_FUNCION",
    "new":"PALABRA_RESERVADA",
    "Scanner":"PALABRA_RESERVADA",
    "System":"PALABRA_RESERVADA",
    "out":"PALABRA_RESERVADA",
    "println":"PALABRA_RESERVADA",
    "class": "PALABRA_RESERVADA",
    "if": "PALABRA_RESERVADA",
    "else": "PALABRA_RESERVADA",
    "do":"PALABRA_RESERVADA",
    "while": "PALABRA_RESERVADA",
    "for": "PALABRA_RESERVADA",
    "switch": "PALABRA_RESERVADA",
    "case": "PALABRA_RESERVADA",
    "break": "PALABRA_RESERVADA",
    "default": "PALABRA_RESERVADA", 
    "true": "PALABRA_RESERVADA",
    "false": "PALABRA_RESERVADA",
    "float": "TIPO_DATO",
    "System": "PALABRA_RESERVADA",
    "private": "MOD_ACCESO",
    "int": "TIPO_DATO",
    "double": "TIPO_DATO",
    "String": "TIPO_DATO",
    "char": "TIPO_DATO",
    "boolean": "TIPO_DATO",
    "long": "TIPO_DATO",
    "short": "TIPO_DATO",
    "return": "PALABRA_RESERVADA",
    "final":"PALABRA_RESERVADA"
}

def t_COMENTARIO(t):
        r'\//.*'
        return t
    
def t_BLOQUE_COMENTARIO(t):
        r'\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/'
        return t
    
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in palabrasReservadas:
        t.type = palabrasReservadas[t.value]
    return t


def t_NUMERO_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERO_DECIMAL(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_CARACTER(t):
    r'\'(.)\''
    t.value = t.group(1)
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t
def t_OPERADOR_INCREMENTO(t):
    r'\+\+'
    return t
def t_OPERADOR_DECREMENTO(t):
    r'\-\-'
    return t

def t_OPERADOR_SUMA(t):
    r'\+'
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

def t_CORCHETE_IZQUIERDO(t):
    r'\['
    return t

def t_CORCHETE_DERECHO(t):
    r'\]'
    return t

def t_PUNTO_COMA(t):
    r'\;'
    return t

def t_COMA(t):
    r'\,'
    return t
def t_DOS_PUNTOS(t):
    r'\:'
    return t

def t_PUNTO(t):
    r'\.'
    return t

def t_ASIGNACION(t):
    r'\='
    return t
def t_MAYOR_IGUA_QUE(t):
    r'\>\='
    return t
def t_MAYOR_QUE(t):
    r'\>'
    return t
def t_MENOR_IGUAL_QUE(t):
    r'\<\='
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

def t_error(t):
    print("Error: caracter desconocido '%s'" % t.value[0])
    t.lexer.skip(1)
    return "".join("Error: caracter desconocido '%s'" % t.value[0])
t_ignore = ' \t\n'

Programa = """
public class HolaMundo {
    private int num = 5;
    public float numero = 3.1;
        System.out.println(numero);
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        System.out.println(num);      
        System.out.println("Hola mundo!");
         if(a >= 5 && numero!=0){
             int ab = -23+3*2/34;
             char c = "a";
         }
    }
}
"""

def analizador_lexico(programa:str)->str:
    analisis = []
    lexer = lex.lex()
    lexer.input(programa)

    while True:
        token = lexer.token()
        if not token:
            break
        analisis.append(str(token)+"\n")
    return "".join(analisis)
