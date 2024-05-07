# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#compilationUnit.
    def visitCompilationUnit(self, ctx:ExprParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx:ExprParser.PackageDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:ExprParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classOrInterfaceDeclaration.
    def visitClassOrInterfaceDeclaration(self, ctx:ExprParser.ClassOrInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classOrInterfaceModifiers.
    def visitClassOrInterfaceModifiers(self, ctx:ExprParser.ClassOrInterfaceModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classOrInterfaceModifier.
    def visitClassOrInterfaceModifier(self, ctx:ExprParser.ClassOrInterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#modifiers.
    def visitModifiers(self, ctx:ExprParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classDeclaration.
    def visitClassDeclaration(self, ctx:ExprParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#normalClassDeclaration.
    def visitNormalClassDeclaration(self, ctx:ExprParser.NormalClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeParameters.
    def visitTypeParameters(self, ctx:ExprParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeParameter.
    def visitTypeParameter(self, ctx:ExprParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeBound.
    def visitTypeBound(self, ctx:ExprParser.TypeBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:ExprParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#enumBody.
    def visitEnumBody(self, ctx:ExprParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#enumConstants.
    def visitEnumConstants(self, ctx:ExprParser.EnumConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#enumConstant.
    def visitEnumConstant(self, ctx:ExprParser.EnumConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#enumBodyDeclarations.
    def visitEnumBodyDeclarations(self, ctx:ExprParser.EnumBodyDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:ExprParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#normalInterfaceDeclaration.
    def visitNormalInterfaceDeclaration(self, ctx:ExprParser.NormalInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeList.
    def visitTypeList(self, ctx:ExprParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classBody.
    def visitClassBody(self, ctx:ExprParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceBody.
    def visitInterfaceBody(self, ctx:ExprParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:ExprParser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#memberDecl.
    def visitMemberDecl(self, ctx:ExprParser.MemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:ExprParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#genericMethodOrConstructorDecl.
    def visitGenericMethodOrConstructorDecl(self, ctx:ExprParser.GenericMethodOrConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#genericMethodOrConstructorRest.
    def visitGenericMethodOrConstructorRest(self, ctx:ExprParser.GenericMethodOrConstructorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:ExprParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:ExprParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceBodyDeclaration.
    def visitInterfaceBodyDeclaration(self, ctx:ExprParser.InterfaceBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceMemberDecl.
    def visitInterfaceMemberDecl(self, ctx:ExprParser.InterfaceMemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceMethodOrFieldDecl.
    def visitInterfaceMethodOrFieldDecl(self, ctx:ExprParser.InterfaceMethodOrFieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceMethodOrFieldRest.
    def visitInterfaceMethodOrFieldRest(self, ctx:ExprParser.InterfaceMethodOrFieldRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#methodDeclaratorRest.
    def visitMethodDeclaratorRest(self, ctx:ExprParser.MethodDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#voidMethodDeclaratorRest.
    def visitVoidMethodDeclaratorRest(self, ctx:ExprParser.VoidMethodDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceMethodDeclaratorRest.
    def visitInterfaceMethodDeclaratorRest(self, ctx:ExprParser.InterfaceMethodDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceGenericMethodDecl.
    def visitInterfaceGenericMethodDecl(self, ctx:ExprParser.InterfaceGenericMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#voidInterfaceMethodDeclaratorRest.
    def visitVoidInterfaceMethodDeclaratorRest(self, ctx:ExprParser.VoidInterfaceMethodDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constructorDeclaratorRest.
    def visitConstructorDeclaratorRest(self, ctx:ExprParser.ConstructorDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constantDeclarator.
    def visitConstantDeclarator(self, ctx:ExprParser.ConstantDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:ExprParser.VariableDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:ExprParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constantDeclaratorsRest.
    def visitConstantDeclaratorsRest(self, ctx:ExprParser.ConstantDeclaratorsRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constantDeclaratorRest.
    def visitConstantDeclaratorRest(self, ctx:ExprParser.ConstantDeclaratorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:ExprParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableInitializer.
    def visitVariableInitializer(self, ctx:ExprParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:ExprParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#modifier.
    def visitModifier(self, ctx:ExprParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#packageOrTypeName.
    def visitPackageOrTypeName(self, ctx:ExprParser.PackageOrTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#enumConstantName.
    def visitEnumConstantName(self, ctx:ExprParser.EnumConstantNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeName.
    def visitTypeName(self, ctx:ExprParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type.
    def visitType(self, ctx:ExprParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx:ExprParser.ClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#primitiveType.
    def visitPrimitiveType(self, ctx:ExprParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableModifier.
    def visitVariableModifier(self, ctx:ExprParser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeArguments.
    def visitTypeArguments(self, ctx:ExprParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeArgument.
    def visitTypeArgument(self, ctx:ExprParser.TypeArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:ExprParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#formalParameters.
    def visitFormalParameters(self, ctx:ExprParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#formalParameterDecls.
    def visitFormalParameterDecls(self, ctx:ExprParser.FormalParameterDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#formalParameterDeclsRest.
    def visitFormalParameterDeclsRest(self, ctx:ExprParser.FormalParameterDeclsRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#methodBody.
    def visitMethodBody(self, ctx:ExprParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constructorBody.
    def visitConstructorBody(self, ctx:ExprParser.ConstructorBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#qualifiedName.
    def visitQualifiedName(self, ctx:ExprParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literal.
    def visitLiteral(self, ctx:ExprParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotations.
    def visitAnnotations(self, ctx:ExprParser.AnnotationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotation.
    def visitAnnotation(self, ctx:ExprParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotationName.
    def visitAnnotationName(self, ctx:ExprParser.AnnotationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#elementValuePairs.
    def visitElementValuePairs(self, ctx:ExprParser.ElementValuePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#elementValuePair.
    def visitElementValuePair(self, ctx:ExprParser.ElementValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#elementValue.
    def visitElementValue(self, ctx:ExprParser.ElementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#elementValueArrayInitializer.
    def visitElementValueArrayInitializer(self, ctx:ExprParser.ElementValueArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotationTypeDeclaration.
    def visitAnnotationTypeDeclaration(self, ctx:ExprParser.AnnotationTypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotationTypeBody.
    def visitAnnotationTypeBody(self, ctx:ExprParser.AnnotationTypeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotationTypeElementDeclaration.
    def visitAnnotationTypeElementDeclaration(self, ctx:ExprParser.AnnotationTypeElementDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotationTypeElementRest.
    def visitAnnotationTypeElementRest(self, ctx:ExprParser.AnnotationTypeElementRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotationMethodOrConstantRest.
    def visitAnnotationMethodOrConstantRest(self, ctx:ExprParser.AnnotationMethodOrConstantRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotationMethodRest.
    def visitAnnotationMethodRest(self, ctx:ExprParser.AnnotationMethodRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotationConstantRest.
    def visitAnnotationConstantRest(self, ctx:ExprParser.AnnotationConstantRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#defaultValue.
    def visitDefaultValue(self, ctx:ExprParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#blockStatement.
    def visitBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#localVariableDeclarationStatement.
    def visitLocalVariableDeclarationStatement(self, ctx:ExprParser.LocalVariableDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:ExprParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableModifiers.
    def visitVariableModifiers(self, ctx:ExprParser.VariableModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#catches.
    def visitCatches(self, ctx:ExprParser.CatchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#catchClause.
    def visitCatchClause(self, ctx:ExprParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#catchType.
    def visitCatchType(self, ctx:ExprParser.CatchTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#finallyBlock.
    def visitFinallyBlock(self, ctx:ExprParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#resourceSpecification.
    def visitResourceSpecification(self, ctx:ExprParser.ResourceSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#resources.
    def visitResources(self, ctx:ExprParser.ResourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#resource.
    def visitResource(self, ctx:ExprParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#formalParameter.
    def visitFormalParameter(self, ctx:ExprParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#switchBlockStatementGroups.
    def visitSwitchBlockStatementGroups(self, ctx:ExprParser.SwitchBlockStatementGroupsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:ExprParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#switchLabel.
    def visitSwitchLabel(self, ctx:ExprParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forControl.
    def visitForControl(self, ctx:ExprParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forInit.
    def visitForInit(self, ctx:ExprParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#enhancedForControl.
    def visitEnhancedForControl(self, ctx:ExprParser.EnhancedForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forUpdate.
    def visitForUpdate(self, ctx:ExprParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parExpression.
    def visitParExpression(self, ctx:ExprParser.ParExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expressionList.
    def visitExpressionList(self, ctx:ExprParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statementExpression.
    def visitStatementExpression(self, ctx:ExprParser.StatementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constantExpression.
    def visitConstantExpression(self, ctx:ExprParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expression.
    def visitExpression(self, ctx:ExprParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:ExprParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:ExprParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#conditionalOrExpression.
    def visitConditionalOrExpression(self, ctx:ExprParser.ConditionalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#conditionalAndExpression.
    def visitConditionalAndExpression(self, ctx:ExprParser.ConditionalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:ExprParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:ExprParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#andExpression.
    def visitAndExpression(self, ctx:ExprParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#equalityExpression.
    def visitEqualityExpression(self, ctx:ExprParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#instanceOfExpression.
    def visitInstanceOfExpression(self, ctx:ExprParser.InstanceOfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relationalExpression.
    def visitRelationalExpression(self, ctx:ExprParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relationalOp.
    def visitRelationalOp(self, ctx:ExprParser.RelationalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#shiftExpression.
    def visitShiftExpression(self, ctx:ExprParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#shiftOp.
    def visitShiftOp(self, ctx:ExprParser.ShiftOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:ExprParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:ExprParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryExpression.
    def visitUnaryExpression(self, ctx:ExprParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryExpressionNotPlusMinus.
    def visitUnaryExpressionNotPlusMinus(self, ctx:ExprParser.UnaryExpressionNotPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#castExpression.
    def visitCastExpression(self, ctx:ExprParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#primary.
    def visitPrimary(self, ctx:ExprParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#identifierSuffix.
    def visitIdentifierSuffix(self, ctx:ExprParser.IdentifierSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#creator.
    def visitCreator(self, ctx:ExprParser.CreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#createdName.
    def visitCreatedName(self, ctx:ExprParser.CreatedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#innerCreator.
    def visitInnerCreator(self, ctx:ExprParser.InnerCreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arrayCreatorRest.
    def visitArrayCreatorRest(self, ctx:ExprParser.ArrayCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classCreatorRest.
    def visitClassCreatorRest(self, ctx:ExprParser.ClassCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#explicitGenericInvocation.
    def visitExplicitGenericInvocation(self, ctx:ExprParser.ExplicitGenericInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#nonWildcardTypeArguments.
    def visitNonWildcardTypeArguments(self, ctx:ExprParser.NonWildcardTypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeArgumentsOrDiamond.
    def visitTypeArgumentsOrDiamond(self, ctx:ExprParser.TypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#nonWildcardTypeArgumentsOrDiamond.
    def visitNonWildcardTypeArgumentsOrDiamond(self, ctx:ExprParser.NonWildcardTypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#selector.
    def visitSelector(self, ctx:ExprParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#superSuffix.
    def visitSuperSuffix(self, ctx:ExprParser.SuperSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#explicitGenericInvocationSuffix.
    def visitExplicitGenericInvocationSuffix(self, ctx:ExprParser.ExplicitGenericInvocationSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arguments.
    def visitArguments(self, ctx:ExprParser.ArgumentsContext):
        return self.visitChildren(ctx)



del ExprParser