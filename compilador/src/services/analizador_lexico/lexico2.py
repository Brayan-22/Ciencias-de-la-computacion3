import ply.lex as lex

class lexico:
    def __init__(self) -> None:
        self.lexer = lex.lex()
        self.tokens = (
            "IDENTIFICADOR",
            "NUMERO_DECIMAL",
            "NUMERO_ENTERO",
            "CARACTER",
            "CADENA",
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
            "COMENTARIO",
            "BLOQUE_COMENTARIO"
            )
        self.palabrasReservadas = {
            "public": "MOD_ACCESO",
            "static": "MODIFICADOR",
            "void": "TIPO_FUNCION",
            "class": "PALABRA_RESERVADA",
            "if": "PALABRA_RESERVADA",
            "else": "PALABRA_RESERVADA",
            "while": "PALABRA_RESERVADA",
            "for": "PALABRA_RESERVADA",
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
            "return": "PALABRA_RESERVADA"
        }
        self.t_ignore = ' \t\n'
    def t_COMENTARIO(self,t):
        r'\//.*'
        return t
    def t_BLOQUE_COMENTARIO(self,t):
        r'\//*.*/'
        return t
    
    def t_IDENTIFICADOR(self,t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value in self.palabrasReservadas:
            t.type = self.palabrasReservadas[t.value]
        return t
    def t_NUMERO_ENTERO(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_NUMERO_DECIMAL(self,t):
        r'\d+(\.\d+)?'
        t.value = float(t.value)
        return t


    def t_CARACTER(self,t):
        r'\'(.)\''
        t.value = t.group(1)
        return t

    def t_CADENA(self,t):
        r'\"([^\\\n]|(\\.))*?\"'
        t.value = t.value[1:-1]
        return t
        
    def t_OPERADOR_SUMA(self,t):
        r'\+'
        return t

    def t_OPERADOR_RESTA(self,t):
        r'-'
        return t

    def t_OPERADOR_MULTIPLICACION(self,t):
        r'\*'
        return t

    def t_OPERADOR_DIVISION(self,t):
        r'/'
        return t

    def t_OPERADOR_LOGICO_AND(self,t):
        r'\&\&'
        return t

    def t_OPERADOR_LOGICO_OR(self,t):
        r'\|\|'
        return t

    def t_DIFERENTE_DE(self,t):
        r'\!='
        return t

    def t_OPERADOR_LOGICO_NOT(self,t):
        r'\!'
        return t

    def t_PARENTESIS_IZQUIERDO(self,t):
        r'\('
        return t

    def t_PARENTESIS_DERECHO(self,t):
        r'\)'
        return t

    def t_LLAVE_IZQUIERDA(self,t):
        r'\{'
        return t

    def t_LLAVE_DERECHA(self,t):
        r'\}'
        return t

    def t_CORCHETE_IZQUIERDO(self,t):
        r'\['
        return t

    def t_CORCHETE_DERECHO(self,t):
        r'\]'
        return t

    def t_PUNTO_COMA(self,t):
        r'\;'
        return t

    def t_COMA(self,t):
        r'\,'
        return t

    def t_PUNTO(self,t):
        r'\.'
        return t

    def t_ASIGNACION(self,t):
        r'\='
        return t

    def t_MAYOR_O_IGUAL_QUE(self,t):
        r'\>='
        return t

    def t_MENOR_O_IGUAL_QUE(self,t):
        r'\<='
        return t

    def t_MAYOR_QUE(self,t):
        r'\>'
        return t

    def t_MENOR_QUE(self,t):
        r'\<'
        return t


    def t_IGUALDAD(self,t):
        r'\=='
        return t
    def t_error(self,t):
        t.lexer.skip(1)
        return "".join("Error: caracter desconocido '%s'" % t.value[0])
    def analizador_lexico(self,programa:str)->str:
        analisis = []
        self.lexer.input(programa)
        while True:
            token = self.lexer.token()
            if not token:
                break
            analisis.append(str(token)+"\n")
        return "".join(analisis)
    

l = lexico()

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

resultado = l.analizador_lexico(Programa)

print(resultado)