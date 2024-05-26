# Generated from MyJava.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyJavaParser import MyJavaParser
else:
    from MyJavaParser import MyJavaParser

# This class defines a complete generic visitor for a parse tree produced by MyJavaParser.

class MyJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyJavaParser#compilationUnit.
    def visitCompilationUnit(self, ctx:MyJavaParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx:MyJavaParser.PackageDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#importDeclaration.
    def visitImportDeclaration(self, ctx:MyJavaParser.ImportDeclarationContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#localVariableDeclaratorList.
    def visitLocalVariableDeclaratorList(self, ctx:MyJavaParser.LocalVariableDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:MyJavaParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)



del MyJavaParser