# Generated from Java.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .JavaParser import JavaParser
else:
    from JavaParser import JavaParser

# This class defines a complete generic visitor for a parse tree produced by JavaParser.

class JavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavaParser#compilationUnit.
    def visitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#importDeclaration.
    def visitImportDeclaration(self, ctx:JavaParser.ImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx:JavaParser.PackageDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:JavaParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classOrInterfaceDeclaration.
    def visitClassOrInterfaceDeclaration(self, ctx:JavaParser.ClassOrInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classOrInterfaceModifiers.
    def visitClassOrInterfaceModifiers(self, ctx:JavaParser.ClassOrInterfaceModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classOrInterfaceModifier.
    def visitClassOrInterfaceModifier(self, ctx:JavaParser.ClassOrInterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#modifiers.
    def visitModifiers(self, ctx:JavaParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#normalClassDeclaration.
    def visitNormalClassDeclaration(self, ctx:JavaParser.NormalClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeParameters.
    def visitTypeParameters(self, ctx:JavaParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeParameter.
    def visitTypeParameter(self, ctx:JavaParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeBound.
    def visitTypeBound(self, ctx:JavaParser.TypeBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:JavaParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumBody.
    def visitEnumBody(self, ctx:JavaParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumConstants.
    def visitEnumConstants(self, ctx:JavaParser.EnumConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumConstant.
    def visitEnumConstant(self, ctx:JavaParser.EnumConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumBodyDeclarations.
    def visitEnumBodyDeclarations(self, ctx:JavaParser.EnumBodyDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#normalInterfaceDeclaration.
    def visitNormalInterfaceDeclaration(self, ctx:JavaParser.NormalInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeList.
    def visitTypeList(self, ctx:JavaParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classBody.
    def visitClassBody(self, ctx:JavaParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceBody.
    def visitInterfaceBody(self, ctx:JavaParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:JavaParser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#memberDecl.
    def visitMemberDecl(self, ctx:JavaParser.MemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#mainMethod.
    def visitMainMethod(self, ctx:JavaParser.MainMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:JavaParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#genericMethodOrConstructorDecl.
    def visitGenericMethodOrConstructorDecl(self, ctx:JavaParser.GenericMethodOrConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#genericMethodOrConstructorRest.
    def visitGenericMethodOrConstructorRest(self, ctx:JavaParser.GenericMethodOrConstructorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceBodyDeclaration.
    def visitInterfaceBodyDeclaration(self, ctx:JavaParser.InterfaceBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceMemberDecl.
    def visitInterfaceMemberDecl(self, ctx:JavaParser.InterfaceMemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceMethodOrFieldDecl.
    def visitInterfaceMethodOrFieldDecl(self, ctx:JavaParser.InterfaceMethodOrFieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceMethodOrFieldRest.
    def visitInterfaceMethodOrFieldRest(self, ctx:JavaParser.InterfaceMethodOrFieldRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#methodDeclaratorRest.
    def visitMethodDeclaratorRest(self, ctx:JavaParser.MethodDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#voidMethodDeclaratorRest.
    def visitVoidMethodDeclaratorRest(self, ctx:JavaParser.VoidMethodDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceMethodDeclaratorRest.
    def visitInterfaceMethodDeclaratorRest(self, ctx:JavaParser.InterfaceMethodDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceGenericMethodDecl.
    def visitInterfaceGenericMethodDecl(self, ctx:JavaParser.InterfaceGenericMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#voidInterfaceMethodDeclaratorRest.
    def visitVoidInterfaceMethodDeclaratorRest(self, ctx:JavaParser.VoidInterfaceMethodDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constructorDeclaratorRest.
    def visitConstructorDeclaratorRest(self, ctx:JavaParser.ConstructorDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constantDeclarator.
    def visitConstantDeclarator(self, ctx:JavaParser.ConstantDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:JavaParser.VariableDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constantDeclaratorsRest.
    def visitConstantDeclaratorsRest(self, ctx:JavaParser.ConstantDeclaratorsRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constantDeclaratorRest.
    def visitConstantDeclaratorRest(self, ctx:JavaParser.ConstantDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:JavaParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableInitializer.
    def visitVariableInitializer(self, ctx:JavaParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:JavaParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#modifier.
    def visitModifier(self, ctx:JavaParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#packageOrTypeName.
    def visitPackageOrTypeName(self, ctx:JavaParser.PackageOrTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumConstantName.
    def visitEnumConstantName(self, ctx:JavaParser.EnumConstantNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeName.
    def visitTypeName(self, ctx:JavaParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#type.
    def visitType(self, ctx:JavaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx:JavaParser.ClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#primitiveType.
    def visitPrimitiveType(self, ctx:JavaParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableModifier.
    def visitVariableModifier(self, ctx:JavaParser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeArguments.
    def visitTypeArguments(self, ctx:JavaParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeArgument.
    def visitTypeArgument(self, ctx:JavaParser.TypeArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:JavaParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#formalParameters.
    def visitFormalParameters(self, ctx:JavaParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#formalParameterDecls.
    def visitFormalParameterDecls(self, ctx:JavaParser.FormalParameterDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#formalParameterDeclsRest.
    def visitFormalParameterDeclsRest(self, ctx:JavaParser.FormalParameterDeclsRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#methodBody.
    def visitMethodBody(self, ctx:JavaParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constructorBody.
    def visitConstructorBody(self, ctx:JavaParser.ConstructorBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#qualifiedName.
    def visitQualifiedName(self, ctx:JavaParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#literal.
    def visitLiteral(self, ctx:JavaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotations.
    def visitAnnotations(self, ctx:JavaParser.AnnotationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotation.
    def visitAnnotation(self, ctx:JavaParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationName.
    def visitAnnotationName(self, ctx:JavaParser.AnnotationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#elementValuePairs.
    def visitElementValuePairs(self, ctx:JavaParser.ElementValuePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#elementValuePair.
    def visitElementValuePair(self, ctx:JavaParser.ElementValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#elementValue.
    def visitElementValue(self, ctx:JavaParser.ElementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#elementValueArrayInitializer.
    def visitElementValueArrayInitializer(self, ctx:JavaParser.ElementValueArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationTypeDeclaration.
    def visitAnnotationTypeDeclaration(self, ctx:JavaParser.AnnotationTypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationTypeBody.
    def visitAnnotationTypeBody(self, ctx:JavaParser.AnnotationTypeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationTypeElementDeclaration.
    def visitAnnotationTypeElementDeclaration(self, ctx:JavaParser.AnnotationTypeElementDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationTypeElementRest.
    def visitAnnotationTypeElementRest(self, ctx:JavaParser.AnnotationTypeElementRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationMethodOrConstantRest.
    def visitAnnotationMethodOrConstantRest(self, ctx:JavaParser.AnnotationMethodOrConstantRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationMethodRest.
    def visitAnnotationMethodRest(self, ctx:JavaParser.AnnotationMethodRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationConstantRest.
    def visitAnnotationConstantRest(self, ctx:JavaParser.AnnotationConstantRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#defaultValue.
    def visitDefaultValue(self, ctx:JavaParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#block.
    def visitBlock(self, ctx:JavaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#blockStatement.
    def visitBlockStatement(self, ctx:JavaParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#localVariableDeclarationStatement.
    def visitLocalVariableDeclarationStatement(self, ctx:JavaParser.LocalVariableDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableModifiers.
    def visitVariableModifiers(self, ctx:JavaParser.VariableModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#statement.
    def visitStatement(self, ctx:JavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#catches.
    def visitCatches(self, ctx:JavaParser.CatchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#catchClause.
    def visitCatchClause(self, ctx:JavaParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#catchType.
    def visitCatchType(self, ctx:JavaParser.CatchTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#finallyBlock.
    def visitFinallyBlock(self, ctx:JavaParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#resourceSpecification.
    def visitResourceSpecification(self, ctx:JavaParser.ResourceSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#resources.
    def visitResources(self, ctx:JavaParser.ResourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#resource.
    def visitResource(self, ctx:JavaParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#formalParameter.
    def visitFormalParameter(self, ctx:JavaParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#switchBlockStatementGroups.
    def visitSwitchBlockStatementGroups(self, ctx:JavaParser.SwitchBlockStatementGroupsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:JavaParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#switchLabel.
    def visitSwitchLabel(self, ctx:JavaParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#forControl.
    def visitForControl(self, ctx:JavaParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#forInit.
    def visitForInit(self, ctx:JavaParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enhancedForControl.
    def visitEnhancedForControl(self, ctx:JavaParser.EnhancedForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#forUpdate.
    def visitForUpdate(self, ctx:JavaParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#parExpression.
    def visitParExpression(self, ctx:JavaParser.ParExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#expressionList.
    def visitExpressionList(self, ctx:JavaParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#statementExpression.
    def visitStatementExpression(self, ctx:JavaParser.StatementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constantExpression.
    def visitConstantExpression(self, ctx:JavaParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#expression.
    def visitExpression(self, ctx:JavaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:JavaParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:JavaParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#conditionalOrExpression.
    def visitConditionalOrExpression(self, ctx:JavaParser.ConditionalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#conditionalAndExpression.
    def visitConditionalAndExpression(self, ctx:JavaParser.ConditionalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:JavaParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:JavaParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#andExpression.
    def visitAndExpression(self, ctx:JavaParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#equalityExpression.
    def visitEqualityExpression(self, ctx:JavaParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#instanceOfExpression.
    def visitInstanceOfExpression(self, ctx:JavaParser.InstanceOfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#relationalExpression.
    def visitRelationalExpression(self, ctx:JavaParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#relationalOp.
    def visitRelationalOp(self, ctx:JavaParser.RelationalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#shiftExpression.
    def visitShiftExpression(self, ctx:JavaParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#shiftOp.
    def visitShiftOp(self, ctx:JavaParser.ShiftOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:JavaParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:JavaParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#unaryExpression.
    def visitUnaryExpression(self, ctx:JavaParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#unaryExpressionNotPlusMinus.
    def visitUnaryExpressionNotPlusMinus(self, ctx:JavaParser.UnaryExpressionNotPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#castExpression.
    def visitCastExpression(self, ctx:JavaParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#primary.
    def visitPrimary(self, ctx:JavaParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#identifierSuffix.
    def visitIdentifierSuffix(self, ctx:JavaParser.IdentifierSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#creator.
    def visitCreator(self, ctx:JavaParser.CreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#createdName.
    def visitCreatedName(self, ctx:JavaParser.CreatedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#innerCreator.
    def visitInnerCreator(self, ctx:JavaParser.InnerCreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#arrayCreatorRest.
    def visitArrayCreatorRest(self, ctx:JavaParser.ArrayCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classCreatorRest.
    def visitClassCreatorRest(self, ctx:JavaParser.ClassCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#explicitGenericInvocation.
    def visitExplicitGenericInvocation(self, ctx:JavaParser.ExplicitGenericInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#nonWildcardTypeArguments.
    def visitNonWildcardTypeArguments(self, ctx:JavaParser.NonWildcardTypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeArgumentsOrDiamond.
    def visitTypeArgumentsOrDiamond(self, ctx:JavaParser.TypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#nonWildcardTypeArgumentsOrDiamond.
    def visitNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaParser.NonWildcardTypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#selector.
    def visitSelector(self, ctx:JavaParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#superSuffix.
    def visitSuperSuffix(self, ctx:JavaParser.SuperSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#explicitGenericInvocationSuffix.
    def visitExplicitGenericInvocationSuffix(self, ctx:JavaParser.ExplicitGenericInvocationSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#arguments.
    def visitArguments(self, ctx:JavaParser.ArgumentsContext):
        return self.visitChildren(ctx)



del JavaParser