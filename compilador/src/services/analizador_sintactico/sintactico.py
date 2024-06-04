import ply.yacc as yacc
import os
import codecs
import re
from analizador_lexico.lexico import tokens


precedence = (
    ('right', 'ASIGNACION'),
    ('left', 'OPERADOR_LOGICO_OR'),
    ('left', 'OPERADOR_LOGICO_AND'),
    ('left', 'DIFERENTE_DE', 'IGUALDAD'),
    ('left', 'MAYOR_QUE', 'MENOR_QUE', 'MAYOR_IGUAL_QUE', 'MENOR_IGUAL_QUE'),
    ('left', 'OPERADOR_SUMA', 'OPERADOR_RESTA'),
    ('left', 'OPERADOR_MULTIPLICACION', 'OPERADOR_DIVISION', 'OPERADOR_MODULO'),
    ('right','NEW', 't_OPERADOR_LOGICO_NOT'),
    ('left', 'PUNTO')
)

''' <program> ::= <block>'''

'''<block> ::= <const-decl><var-decl><proc-decl><statement>'''

'''<const-decl>::= const <const-assignment-list>; | e'''

def p_program(p):
    ''' program = block '''
    #p[0] = program(p[1],"program")


def p_constDecl(p):
    '''constDecl = CONST constAssignment-list ;'''
    #p[0] = constDecl(p[2],"constAssignmentList")
    
def p_constDeclEmpty(p):
    '''constDecl = empty'''
    #p[0] = NULL()

def p_compilationUnit(p):
    '''compilationUnit = packageDecl importDecl typeDecl'''
    
    
"<programa> ::= { <declaracion> }"

def p_program(p):
    print("programa")
    
def declaracion