grammar MyJava;

// Regla principal
compilationUnit
    :   packageDeclaration? importDeclaration* typeDeclaration* EOF
    ;

// Declaración de paquete
packageDeclaration
    :   PACKAGE qualifiedName PUNTOCOMA
    ;

// Declaración de importación
importDeclaration
    :   IMPORT qualifiedName (PUNTO ASTERISCO)? PUNTOCOMA
    ;

// Declaración de tipo (en este caso, solo clases)
typeDeclaration
    :   classDeclaration
    ;

// Declaración de clase
classDeclaration
    :   classModifier* CLASS Identifier LLAVEIZQ classBody LLAVEDER
    ;

// Modificadores de clase
classModifier
    :   PUBLIC
    |   PROTECTED
    |   PRIVATE
    |   ABSTRACT
    |   STATIC
    |   FINAL
    ;

// Cuerpo de la clase (aquí se puede extender para agregar más reglas)
classBody
    :   (classBodyDeclaration)*
    ;

// Declaraciones dentro del cuerpo de la clase
classBodyDeclaration
    :   classVariableDeclaration
    |   methodDeclaration
    |   mainMethodDeclaration
    |   PUNTOCOMA // Esto es solo un marcador de posición, aquí se agregarían métodos, etc.
    ;
mainMethodDeclaration
    :   PUBLIC STATIC VOID MAIN PARENIZQ type CORCHIZQ CORCHDER Identifier PARENDER methodBody
    ;
methodDeclaration
    :   memberModifier* typeOrVoid methodDeclarator methodBody
    ;
    
methodDeclarator
    :   methodInitializer PARENIZQ formalParameters PARENDER
    ;
methodInitializer
    :   Identifier
    ;

// Declaraciones de variables de clase
classVariableDeclaration
    :   memberModifier* type variableDeclaratorList PUNTOCOMA
    ;
typeOrVoid
    :   type
    |   VOID
    ;

// Parámetros formales
formalParameters
    :   (formalParameterList)?
    ;
// Modificadores de variables
variableModifier
    : FINAL
    ;
// Lista de parámetros formales
formalParameterList
    :   formalParameter (COMA formalParameter)*
    ;

// Parámetro formal
formalParameter
    :   variableModifier* type variableDeclaratorId
    ;

// Identificador del declarador de variable
variableDeclaratorId
    :   Identifier
    ;

// Cuerpo del método
methodBody
    :   block
    ;

// Bloque de código
block
    :   LLAVEIZQ blockStatement* LLAVEDER
    ;

// Declaraciones dentro de un bloque
blockStatement
    :   localVariableDeclarationStatement
    |   statement
    ;

// Declaración de variables locales
localVariableDeclarationStatement
    :   variableModifier? type localVariableDeclaratorList PUNTOCOMA
    ;
localVariableDeclaration
    :   variableModifier? type localVariableDeclaratorList
    ;
// Sentencia
statement
    :   block
    |   ifStatement
    |   whileStatement
    |   doWhileStatement
    |   forStatement
    |   switchStatement
    |   breakStatement
    |   expressionStatement
    |   PUNTOCOMA
    ;
expressionStatement
    :   expression PUNTOCOMA
    ;
// Sentencia if
ifStatement
    :   IF PARENIZQ booleanExpression PARENDER statement (ELSE statement)?
    ;
// Sentencia while
whileStatement
    :   WHILE PARENIZQ booleanExpression PARENDER statement
    ;
    
// Sentencia do-while
doWhileStatement
    :   DO statement WHILE PARENIZQ expression PARENDER PUNTOCOMA
    ;

// Sentencia for
forStatement
    :   FOR PARENIZQ forControl PARENDER statement
    ;


// Control de la sentencia for
forControl
    :   forInit? PUNTOCOMA booleanExpression? PUNTOCOMA forUpdate?
    ;

// Inicialización de la sentencia for
forInit
    :   localVariableDeclaration
    |   expressionList
    ;

// Actualización de la sentencia for
forUpdate
    :   expressionList
    ;

switchStatement
    :   SWITCH PARENIZQ expression PARENDER switchBlock
    ;

switchBlock
    :   LLAVEIZQ switchBlockStatementGroup* switchLabel* LLAVEDER
    ;

switchBlockStatementGroup
    :   switchLabel+ blockStatement*
    ;

switchLabel
    :   CASE expression DOSPUNTOS
    |   DEFAULT DOSPUNTOS
    ;

breakStatement
    :   BREAK PUNTOCOMA
    ;

// Lista de expresiones
expressionList
    :   expression (COMA expression)*
    ;
// Expresión booleana
booleanExpression
    :   expression (relationalOperator expression)?
    ;
// Operadores relacionales
relationalOperator
    :   MAYOR
    |   MENOR
    |   MAYORIGUAL
    |   MENORIGUAL
    |   IGUALIGUAL
    |   DISTINTO
    ;
// Modificadores de variables
memberModifier
    :   PUBLIC
    |   PROTECTED
    |   PRIVATE
    |   STATIC
    |   FINAL
    ;

// Tipo de variable
type
    :   primitiveType
    |   qualifiedName
    ;

// Tipos primitivos
primitiveType
    :   BOOLEAN
    |   CHAR
    |   BYTE
    |   SHORT
    |   INT
    |   LONG
    |   FLOAT
    |   DOUBLE
    |   STRING
    ;

// Lista de declaradores de variables
variableDeclaratorList
    :   variableDeclarator (COMA variableDeclarator)*
    ;
localVariableDeclaratorList
    :   variableDeclarator (COMA variableDeclarator)*
    ;
// Declarador de variable
variableDeclarator
    :   Identifier (IGUAL variableInitializer)?
    ;

// Inicializador de variable
variableInitializer
    :   expression
    ;

expression
    :   literal
    |   Identifier
    |   Identifier IGUAL expression
    |   expression MAYOR expression
    |   expression MENOR expression
    |   expression MAYORIGUAL expression
    |   expression MENORIGUAL expression
    |   expression IGUALIGUAL expression
    |   expression DISTINTO expression
    |   expression MAS expression
    |   expression MENOS expression
    |   expression ASTERISCO expression
    |   expression DIV expression
    |   expression MASMAS
    |   expression MENOSMENOS
    |   PARENIZQ expression PARENDER
    ;

// Literales
literal
    :   INTEGER_LITERAL
    |   FLOAT_LITERAL
    |   CHAR_LITERAL
    |   STRING_LITERAL
    |   BOOLEAN_LITERAL
    ;

// Nombres calificados (para paquetes e importaciones)
qualifiedName
    :   Identifier (PUNTO Identifier)*
    ;


// Tokens básicos
PACKAGE: 'package';
IMPORT: 'import';
CLASS: 'class';
PUBLIC: 'public';
PROTECTED: 'protected';
PRIVATE: 'private';
ABSTRACT: 'abstract';
STATIC: 'static';
FINAL: 'final';
BOOLEAN: 'boolean';
CHAR: 'char';
BYTE: 'byte';
SHORT: 'short';
INT: 'int';
LONG: 'long';
FLOAT: 'float';
DOUBLE: 'double';
STRING:'String';
PUNTO: '.';
PUNTOCOMA: ';';
COMA: ',';
IGUAL: '=';
LLAVEIZQ: '{';
LLAVEDER: '}';
CORCHIZQ:'[';
CORCHDER:']';
PARENIZQ:'(';
PARENDER:')';
DOSPUNTOS:':';
VOID:'void';
MAIN:'main';
IF:'if';
ELSE:'else';
WHILE:'while';
DO:'do';
FOR:'for';
MAYOR: '>';
MENOR: '<';
MAYORIGUAL: '>=';
MENORIGUAL: '<=';
IGUALIGUAL: '==';
DISTINTO: '!=';
MASMAS : '++';
MENOSMENOS : '--';
MAS:'+';
MENOS:'-';
ASTERISCO:'*';
DIV:'/';
SWITCH:'switch';
CASE:'case';
DEFAULT:'default';
BREAK:'break';
// Literales
INTEGER_LITERAL: [0-9]+;
FLOAT_LITERAL: [0-9]+'.'[0-9]*;
CHAR_LITERAL: '\'' . '\'';
STRING_LITERAL: '"' .*? '"';
BOOLEAN_LITERAL: 'true' | 'false';

// Identificadores
Identifier
    :   JavaLetter JavaLetterOrDigit*
    ;

// Letras válidas para identificadores en Java
fragment JavaLetter
    :   [a-zA-Z$_]
    ;

// Dígitos válidos para identificadores en Java
fragment JavaLetterOrDigit
    :   [a-zA-Z0-9$_]
    ;

COMMENT      : '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT : '//' ~[\r\n]*    -> channel(HIDDEN);


// Ignorar espacios en blanco y comentarios
WS
    :   [ \t\r\n]+ -> skip
    ;