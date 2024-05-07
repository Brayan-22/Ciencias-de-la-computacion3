import ply.yacc as yacc

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

precedence = (
    ('left', 'OPERADOR_MULTIPLICACION', 'OPERADOR_DIVISION'),
    ('left', 'OPERADOR_SUMA', 'OPERADOR_RESTA'),
    ('left', 'MAYOR_QUE', 'MENOR_QUE', 'MAYOR_O_IGUAL_QUE', 'MENOR_O_IGUAL_QUE', 'IGUALDAD', 'DIFERENTE_DE'),
)

def p_programa(p):
    '''programa : bloque'''
    p[0] = p[1]

def p_bloque(p):
    '''bloque : lista_declaraciones '{' lista_sentencias '}' '''
    p[0] = {'declaraciones': p[1], 'sentencias': p[3]}

def p_lista_declaraciones(p):
    '''lista_declaraciones : declaracion ';' lista_declaraciones'''
    p[0] = [p[1]] + p[3]
def p_lista_declaraciones_vacias(p):
    '''lista_declaraciones : '''
    p[0] = []

def p_declaracion(p):
    '''
    declaracion : tipo_dato variable
                | tipo_dato variable ASIGNACION expresion
    '''
    p[0] = {'tipo_dato': p[1], 'variable': p[2]}
    if len(p) > 3:
        p[0]['expresion'] = p[4]

def p_tipo_dato(p):
    '''tipo_dato : INT 
                 | FLOAT 
                 | VOID'''
    p[0] = p[1]

def p_variable(p):
    '''variable : IDENTIFICADOR'''
    p[0] = p[1]

def p_lista_sentencias(p):
    '''lista_sentencias : sentencia lista_sentencias'''
    p[0] = [p[1]] + p[2]
def p_lista_sentencias_vacias(p):
    '''lista_sentencias : '''
    p[0] = []

def p_sentencia(p):
    '''sentencia : declaracion_asignacion ';'
                 | sentencia_if
                 | sentencia_while
                 | sentencia_for
                 | sentencia_return
                 | sentencia_imprimir
                 | bloque
                 | ';'
    '''
    p[0] = p[1]

def p_declaracion_asignacion(p):
    '''declaracion_asignacion : variable ASIGNACION expresion'''
    p[0] = {'variable': p[1], 'expresion': p[3]}

def p_sentencia_if(p):
    '''
    sentencia_if : IF expresion bloque
                 | IF expresion bloque ELSE bloque
    '''
    if len(p) == 4:
        p[0] = {'condicion': p[2], 'bloque': p[3]}
    else:
        p[0] = {'condicion': p[2], 'bloque_if': p[3], 'bloque_else': p[5]}

def p_sentencia_while(p):
    '''
    sentencia_while : WHILE expresion bloque
    '''
    p[0] = {'condicion': p[2], 'bloque': p[3]}

def p_sentencia_for(p):
    '''
    sentencia_for : FOR PARENTESIS_IZQUIERDO declaracion_asignacion PUNTO_COMA expresion PUNTO_COMA incremento_decremento PARENTESIS_DERECHO bloque
    '''
    p[0] = {'inicializacion': p[3], 'condicion': p[5], 'incremento_decremento': p[7], 'bloque': p[9]}

def p_incremento_decremento(p):
    '''incremento_decremento : variable OPERADOR_SUMA NUMERO_ENTERO
                             | variable OPERADOR_RESTA NUMERO_ENTERO
    '''
    p[0] = {'variable': p[1], 'operador': p[2], 'valor': p[3]}

def p_sentencia_return(p):
    '''
    sentencia_return : RETURN expresion PUNTO_COMA
                     | RETURN PUNTO_COMA
    '''
    if len(p) == 4:
        p[0] = {'tipo': 'retorno', 'expresion': p[2]}
    else:
        p[0] = {'tipo': 'retorno', 'expresion': None}

def p_sentencia_imprimir(p):
    '''
    sentencia_imprimir : IMPRIMIR PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO PUNTO_COMA
                       | IMPRIMIR PARENTESIS_IZQUIERDO CADENA PARENTESIS_DERECHO PUNTO_COMA
    '''
    if len(p) == 6:  # Imprimir una expresión
        p[0] = {'tipo': 'imprimir_expresion', 'expresion': p[3]}
    else:  # Imprimir una cadena
        p[0] = {'tipo': 'imprimir_cadena', 'cadena': p[3]}

def p_expresion(p):
    '''expresion : expresion_simple OPERADOR_RELACIONAL expresion_simple
                 | expresion_simple
    '''
    if len(p) == 4:
        p[0] = {'operador_relacional': p[2], 'izquierda': p[1], 'derecha': p[3]}
    else:
        p[0] = p[1]

def p_expresion_simple(p):
    '''expresion_simple : termino '+' termino
                        | termino '-' termino
                        | termino
    '''
    if len(p) == 4:
        p[0] = {'operador': p[2], 'izquierda': p[1], 'derecha': p[3]}
    else:
        p[0] = p[1]

def p_termino(p):
    '''termino : factor '*' 
               | factor '/' factor
               | factor
    '''
    if len(p) == 4:
        p[0] = {'operador': p[2], 'izquierda': p[1], 'derecha': p[3]}
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : IDENTIFICADOR
             | NUMERO_ENTERO
             | NUMERO_DECIMAL
             | CADENA
             | CARACTER
             | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
             | NOT factor
    '''
    if p[1] in ['IDENTIFICADOR', 'NUMERO_ENTERO', 'NUMERO_DECIMAL', 'CADENA', 'CARACTER']:
        p[0] = p[1]
    elif len(p) == 4:  # expresión entre paréntesis
        p[0] = p[2]
    else:  # operador NOT
        p[0] = {'operador': 'NOT', 'operando': p[2]}

def p_error(p):
    print("Error sintáctico en la línea", p.lineno, "cerca de", p.value)
    
parser = yacc.yacc()