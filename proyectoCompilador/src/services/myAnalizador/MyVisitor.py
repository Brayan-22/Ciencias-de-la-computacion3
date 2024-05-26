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
        self.localVar={
        }
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
            h["type"]=ctx.type_().getText()
            temp = "----Dec y Asig------\nSintaxis correcta\n";
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
                if h["type"] != self.classVar[h["id"]]["type"]:
                    raise SemanticErrorException(f"Error de semantica. Tipos invalidos:{h["type"]} incompatible {self.classVar[h["id"]]["type"]}")
                else:
                    self.classVar[h["id"]]["value"] = h['value']
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
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#whileStatement.
    def visitWhileStatement(self, ctx:MyJavaParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:MyJavaParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forStatement.
    def visitForStatement(self, ctx:MyJavaParser.ForStatementContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchBlock.
    def visitSwitchBlock(self, ctx:MyJavaParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:MyJavaParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchLabel.
    def visitSwitchLabel(self, ctx:MyJavaParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#breakStatement.
    def visitBreakStatement(self, ctx:MyJavaParser.BreakStatementContext):
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

        
