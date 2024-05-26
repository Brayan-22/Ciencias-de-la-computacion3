import sys
from antlr4 import *

from services.myantlr4.MyJavaParser import MyJavaParser as MyJavaParser
from services.myantlr4.MyJavaVisitor import MyJavaVisitor as MyJavaVisitor
class SemanticErrorException(Exception):
    def __init__(self, message):
        super().__init__(message)

class VisitorInterp(MyJavaVisitor):
    def __init__(self) -> None:
        self.classVar = {}
        self.localVar={}
        self.analisiSintactico = []
    def getAnalsis(self)->list:
        return self.analisiSintactico
        
# Visit a parse tree produced by MyJavaParser#compilationUnit.
    def visitCompilationUnit(self, ctx:MyJavaParser.CompilationUnitContext):
        print("SE INICIA EL ANALISIS SINTACTICO")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx:MyJavaParser.PackageDeclarationContext):
        temp = (f"{ctx.PACKAGE().getText()} {self.visitQualifiedName(ctx.qualifiedName())}{ctx.PUNTOCOMA().getText()}")
        temp2 ="------paquete-----\nSintaxis correcta\n"
        self.analisiSintactico.append(temp2+temp+"\n")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#importDeclaration.
    def visitImportDeclaration(self, ctx:MyJavaParser.ImportDeclarationContext):
        temp = (f"{ctx.IMPORT().getText()} {self.visitQualifiedName(ctx.qualifiedName())}{ctx.PUNTOCOMA().getText()}")
        temp2 ="------import-----\nSintaxis correcta\n"
        self.analisiSintactico.append(temp2+temp+"\n")
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by MyJavaParser#ioStatement.
    def visitIoStatement(self, ctx:MyJavaParser.IoStatementContext):     
        temp = ""
        if ctx.printStatement() is not None:
            temp = (f"{ctx.printStatement().getText()}")
        if ctx.scanStatement() is not None:
            temp = (f"{ctx.scanStatement().getText()}")
        temp2 ="------IO-----\nSintaxis correcta\n"
        self.analisiSintactico.append(temp2+temp+"\n")   
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#printStatement.
    def visitPrintStatement(self, ctx:MyJavaParser.PrintStatementContext):

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#scanStatement.
    def visitScanStatement(self, ctx:MyJavaParser.ScanStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyJavaParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:MyJavaParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MyJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classModifier.
    def visitClassModifier(self, ctx:MyJavaParser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classBody.
    def visitClassBody(self, ctx:MyJavaParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:MyJavaParser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#mainMethodDeclaration.
    def visitMainMethodDeclaration(self, ctx:MyJavaParser.MainMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MyJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodDeclarator.
    def visitMethodDeclarator(self, ctx:MyJavaParser.MethodDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodInitializer.
    def visitMethodInitializer(self, ctx:MyJavaParser.MethodInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classVariableDeclaration.
    def visitClassVariableDeclaration(self, ctx:MyJavaParser.ClassVariableDeclarationContext):
        #Declaracion de variables de clase
        acceso =[]
        for modifier in ctx.memberModifier():
            acceso.append(modifier.getText())
        hola = self.visitVariableDeclaratorList(ctx.variableDeclaratorList())
        for h in hola:
            h["modifiers"] = acceso
            
            if ctx.type_() is not None:
                h["type"]=ctx.type_().getText()
            else:
                h["type"]=""
            temp = "----Dec y Asig------\nSintaxis correcta\n"
            classVarAnalisis = []
            classVarAnalisis.extend(acceso)
            classVarAnalisis.append(h["type"])
            classVarAnalisis.extend(h["as"])
            if 'value' not in h:
                h['value'] = None
            temp2 = ' '.join(classVarAnalisis)
            self.analisiSintactico.append(temp+temp2+";"+"\n")
            del h["as"]
        
        for h in hola:
            if h["id"] in self.classVar:
                if h["type"] == self.classVar[h["id"]]["type"]:
                    self.classVar[h["id"]]["value"] = h['value']
                elif h["type"] != self.classVar[h["id"]]["type"] and h["type"]=="" :
                    tempV = h["value"]
                    if self.classVar[h["id"]]["type"] == "int":
                        try:
                            tempV = int(tempV)
                            self.classVar[h["id"]]["value"] = h['value']
                        except ValueError as _:
                            raise SemanticErrorException(f"Error de semantica. Tipos incompatibles")
                    else:
                        pass
                else:
                    tipo1 = self.classVar[h["id"]]["type"]
                    tipo2 = str(h["type"])
                    raise SemanticErrorException(f"Error de semantica. Tipos invalidos:{tipo2} incompatible {tipo1}")
            else:
                if h["type"]=="":
                    raise SemanticErrorException(f"Error de semantica. No declaracion de tipo")
                else:
                    self.classVar[h["id"]] ={
                    "type":h["type"],
                    "value":h["value"]
                    }
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeOrVoid.
    def visitTypeOrVoid(self, ctx:MyJavaParser.TypeOrVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#formalParameters.
    def visitFormalParameters(self, ctx:MyJavaParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableModifier.
    def visitVariableModifier(self, ctx:MyJavaParser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#formalParameterList.
    def visitFormalParameterList(self, ctx:MyJavaParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#formalParameter.
    def visitFormalParameter(self, ctx:MyJavaParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:MyJavaParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodBody.
    def visitMethodBody(self, ctx:MyJavaParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#block.
    def visitBlock(self, ctx:MyJavaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#blockStatement.
    def visitBlockStatement(self, ctx:MyJavaParser.BlockStatementContext):
        
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#localVariableDeclarationStatement.
    def visitLocalVariableDeclarationStatement(self, ctx:MyJavaParser.LocalVariableDeclarationStatementContext):
        #aca termina toda la logica de local var
        acceso = ""
        if ctx.variableModifier() is not None:
            acceso=ctx.variableModifier().getText()
        hola = self.visitLocalVariableDeclaratorList(ctx.localVariableDeclaratorList());
        for h in hola:
            h["modifiers"] = acceso
            if ctx.type_() is not None:
                h["type"]=ctx.type_().getText()
            else:
                h["type"]=""
            temp = "----Local Dec y Asig------\nSintaxis correcta\n"
            localVarAnalisis=[]
            localVarAnalisis.append(acceso)
            localVarAnalisis.append(h["type"])
            localVarAnalisis.extend(h["as"])
            if 'value' not in h:
                h['value'] = None
            temp2 = ' '.join(localVarAnalisis)
            self.analisiSintactico.append(temp+temp2+";"+"\n")
            del h["as"]

        for h in hola:
            if h["id"] in self.localVar:
                if h["type"] == self.localVar[h["id"]]["type"]:
                    self.localVar[h["id"]]["value"] = h['value']
                elif h["type"] != self.localVar[h["id"]]["type"] and h["type"]=="" :
                    tempV = h["value"]
                    if self.localVar[h["id"]]["type"] == "int":
                        try:
                            tempV = int(tempV)
                            self.localVar[h["id"]]["value"] = h['value']
                        except ValueError as _:
                            raise SemanticErrorException(f"Error de semantica. Tipos incompatibles")
                    else:
                        pass
                else:
                    tipo1 = self.localVar[h["id"]]["type"]
                    tipo2 = str(h["type"])
                    raise SemanticErrorException(f"Error de semantica. Tipos invalidos:{tipo2} incompatible {tipo1}")
            else:
                if h["type"]=="":
                    raise SemanticErrorException(f"Error de semantica. No declaracion de tipo")
                else:
                    self.localVar[h["id"]] ={
                    "type":h["type"],
                    "value":h["value"]
                    }
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by MyJavaParser#localVariableDeclaratorList.
    def visitLocalVariableDeclaratorList(self, ctx:MyJavaParser.LocalVariableDeclaratorListContext):
        listaVariables = []
        for varDec in ctx.variableDeclarator():
            listaVariables.append(self.visitVariableDeclarator(varDec))
        return listaVariables


    # Visit a parse tree produced by MyJavaParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:MyJavaParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#statement.
    def visitStatement(self, ctx:MyJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MyJavaParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#ifStatement.
    def visitIfStatement(self, ctx:MyJavaParser.IfStatementContext):
        temp = f"------SENTENCIA IF--------\nSintaxis correcta\n"
        temp2 =""
        if ctx.ELSE() is None:
            temp2=ctx.IF().getText()+"("+ctx.booleanExpression().getText()+")"+"{"+"...sentencia..." +"}"
        else:
            temp2=ctx.IF().getText()+"("+ctx.booleanExpression().getText()+")"+"{"+"...sentencia..." +"}"+ctx.ELSE().getText()+"{"+"...sentencia..."+"}"
        self.analisiSintactico.append(temp+temp2+"\n")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#whileStatement.
    def visitWhileStatement(self, ctx:MyJavaParser.WhileStatementContext):
        temp = "...Sentencia while...\nSintaxis Correcta\n"
        temp2 = ctx.WHILE().getText()+"("+ctx.booleanExpression().getText()+")"+ctx.statement().getText()
        self.analisiSintactico.append(temp+temp2+"\n")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:MyJavaParser.DoWhileStatementContext):
        temp = "...Sentencia do while...\nSintaxis Correcta\n"
        temp2 = ctx.DO().getText()+ctx.statement().getText()+ctx.WHILE().getText()+"("+ctx.expression().getText()+")"+";"
        self.analisiSintactico.append(temp+temp2+"\n")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forStatement.
    def visitForStatement(self, ctx:MyJavaParser.ForStatementContext):
        temp = "...Sentencia for...\nSintaxis Correcta\n"
        temp2 = ctx.FOR().getText()+"("+ctx.forControl().getText()+")"+"\n"+ctx.statement().getText()
        self.analisiSintactico.append(temp+temp2+"\n")
        return self.visitChildren(ctx)
        
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forControl.
    def visitForControl(self, ctx:MyJavaParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forInit.
    def visitForInit(self, ctx:MyJavaParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forUpdate.
    def visitForUpdate(self, ctx:MyJavaParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchStatement.
    def visitSwitchStatement(self, ctx:MyJavaParser.SwitchStatementContext):
        temp = "...Sentencia Switch...\nSintaxis correcta\n"
        swB = self.visitSwitchBlock(ctx.switchBlock())
        temp2 = "\n".join(swB)
        temp3 = f"{ctx.SWITCH().getText()} ({ctx.expression().getText()}) {temp2}"
        self.analisiSintactico.append(temp+temp3+"\n")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchBlock.
    def visitSwitchBlock(self, ctx:MyJavaParser.SwitchBlockContext):
        #------------
        grupoSwitch = []
        grupoSwitch.append(ctx.LLAVEIZQ().getText())
        for sbsg in ctx.switchBlockStatementGroup():
            grupoSwitch.append(sbsg.getText())
        grupoSwitch.append(ctx.LLAVEDER().getText())
        return grupoSwitch


    # Visit a parse tree produced by MyJavaParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:MyJavaParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchLabel.
    def visitSwitchLabel(self, ctx:MyJavaParser.SwitchLabelContext):
        # if ctx.CASE() is None:
        #     return ctx.DEFAULT().getText()+ctx.DOSPUNTOS().getText()
        # else:
        #     return ctx.CASE().getText()+ctx.expression().getText()+ctx.DOSPUNTOS().getText()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyJavaParser#breakStatement.
    def visitBreakStatement(self, ctx:MyJavaParser.BreakStatementContext):
        # return ctx.getText()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#expressionList.
    def visitExpressionList(self, ctx:MyJavaParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#booleanExpression.
    def visitBooleanExpression(self, ctx:MyJavaParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#relationalOperator.
    def visitRelationalOperator(self, ctx:MyJavaParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#memberModifier.
    def visitMemberModifier(self, ctx:MyJavaParser.MemberModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#type.
    def visitType(self, ctx:MyJavaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#primitiveType.
    def visitPrimitiveType(self, ctx:MyJavaParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableDeclaratorList.
    def visitVariableDeclaratorList(self, ctx:MyJavaParser.VariableDeclaratorListContext):
        #lista de variables
        listaVariables = []
        for varDec in ctx.variableDeclarator():
            listaVariables.append(self.visitVariableDeclarator(varDec))
        return listaVariables


    # Visit a parse tree produced by MyJavaParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:MyJavaParser.VariableDeclaratorContext):
        variableDec = {}
        temp = f"{ctx.Identifier().getText()}"
        variableDec["id"] = temp
        if ctx.IGUAL() is None:
            variableDec["as"] = [temp]
            return variableDec
        else:
            temp2 = ctx.IGUAL().getText()
            temp3 = ctx.variableInitializer().getText()
            variableDec["value"]=temp3
            variableDec["as"] = [temp,temp2,temp3]
            return variableDec


    # Visit a parse tree produced by MyJavaParser#variableInitializer.
    def visitVariableInitializer(self, ctx:MyJavaParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#expression.
    def visitExpression(self, ctx:MyJavaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#literal.
    def visitLiteral(self, ctx:MyJavaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#qualifiedName.
    def visitQualifiedName(self, ctx:MyJavaParser.QualifiedNameContext):
        qualifiedNames = []
        qualifiedName = ""
        for id in ctx.Identifier():
            qualifiedNames.append(id.getText())
        qualifiedName = '.'.join(qualifiedNames)
        return qualifiedName

        
