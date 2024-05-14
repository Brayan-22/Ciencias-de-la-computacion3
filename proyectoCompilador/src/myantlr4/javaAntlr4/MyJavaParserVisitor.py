# Generated from MyJavaParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyJavaParser import MyJavaParser
else:
    from MyJavaParser import MyJavaParser

# This class defines a complete generic visitor for a parse tree produced by MyJavaParser.

class MyJavaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyJavaParser#start_.
    def visitStart_(self, ctx:MyJavaParser.Start_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#literal.
    def visitLiteral(self, ctx:MyJavaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeIdentifier.
    def visitTypeIdentifier(self, ctx:MyJavaParser.TypeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unqualifiedMethodIdentifier.
    def visitUnqualifiedMethodIdentifier(self, ctx:MyJavaParser.UnqualifiedMethodIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#primitiveType.
    def visitPrimitiveType(self, ctx:MyJavaParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#numericType.
    def visitNumericType(self, ctx:MyJavaParser.NumericTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#integralType.
    def visitIntegralType(self, ctx:MyJavaParser.IntegralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#floatingPointType.
    def visitFloatingPointType(self, ctx:MyJavaParser.FloatingPointTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#referenceType.
    def visitReferenceType(self, ctx:MyJavaParser.ReferenceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#coit.
    def visitCoit(self, ctx:MyJavaParser.CoitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx:MyJavaParser.ClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classType.
    def visitClassType(self, ctx:MyJavaParser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceType.
    def visitInterfaceType(self, ctx:MyJavaParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeVariable.
    def visitTypeVariable(self, ctx:MyJavaParser.TypeVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#arrayType.
    def visitArrayType(self, ctx:MyJavaParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#dims.
    def visitDims(self, ctx:MyJavaParser.DimsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeParameter.
    def visitTypeParameter(self, ctx:MyJavaParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeParameterModifier.
    def visitTypeParameterModifier(self, ctx:MyJavaParser.TypeParameterModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeBound.
    def visitTypeBound(self, ctx:MyJavaParser.TypeBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#additionalBound.
    def visitAdditionalBound(self, ctx:MyJavaParser.AdditionalBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeArguments.
    def visitTypeArguments(self, ctx:MyJavaParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeArgumentList.
    def visitTypeArgumentList(self, ctx:MyJavaParser.TypeArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeArgument.
    def visitTypeArgument(self, ctx:MyJavaParser.TypeArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#wildcard.
    def visitWildcard(self, ctx:MyJavaParser.WildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#wildcardBounds.
    def visitWildcardBounds(self, ctx:MyJavaParser.WildcardBoundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#moduleName.
    def visitModuleName(self, ctx:MyJavaParser.ModuleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#packageName.
    def visitPackageName(self, ctx:MyJavaParser.PackageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeName.
    def visitTypeName(self, ctx:MyJavaParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#packageOrTypeName.
    def visitPackageOrTypeName(self, ctx:MyJavaParser.PackageOrTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#expressionName.
    def visitExpressionName(self, ctx:MyJavaParser.ExpressionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodName.
    def visitMethodName(self, ctx:MyJavaParser.MethodNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#ambiguousName.
    def visitAmbiguousName(self, ctx:MyJavaParser.AmbiguousNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#compilationUnit.
    def visitCompilationUnit(self, ctx:MyJavaParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#ordinaryCompilationUnit.
    def visitOrdinaryCompilationUnit(self, ctx:MyJavaParser.OrdinaryCompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#modularCompilationUnit.
    def visitModularCompilationUnit(self, ctx:MyJavaParser.ModularCompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx:MyJavaParser.PackageDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#packageModifier.
    def visitPackageModifier(self, ctx:MyJavaParser.PackageModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#importDeclaration.
    def visitImportDeclaration(self, ctx:MyJavaParser.ImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#singleTypeImportDeclaration.
    def visitSingleTypeImportDeclaration(self, ctx:MyJavaParser.SingleTypeImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeImportOnDemandDeclaration.
    def visitTypeImportOnDemandDeclaration(self, ctx:MyJavaParser.TypeImportOnDemandDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#singleStaticImportDeclaration.
    def visitSingleStaticImportDeclaration(self, ctx:MyJavaParser.SingleStaticImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#staticImportOnDemandDeclaration.
    def visitStaticImportOnDemandDeclaration(self, ctx:MyJavaParser.StaticImportOnDemandDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#topLevelClassOrInterfaceDeclaration.
    def visitTopLevelClassOrInterfaceDeclaration(self, ctx:MyJavaParser.TopLevelClassOrInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#moduleDeclaration.
    def visitModuleDeclaration(self, ctx:MyJavaParser.ModuleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#moduleDirective.
    def visitModuleDirective(self, ctx:MyJavaParser.ModuleDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#requiresModifier.
    def visitRequiresModifier(self, ctx:MyJavaParser.RequiresModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MyJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#normalClassDeclaration.
    def visitNormalClassDeclaration(self, ctx:MyJavaParser.NormalClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classModifier.
    def visitClassModifier(self, ctx:MyJavaParser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeParameters.
    def visitTypeParameters(self, ctx:MyJavaParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeParameterList.
    def visitTypeParameterList(self, ctx:MyJavaParser.TypeParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classExtends.
    def visitClassExtends(self, ctx:MyJavaParser.ClassExtendsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classImplements.
    def visitClassImplements(self, ctx:MyJavaParser.ClassImplementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceTypeList.
    def visitInterfaceTypeList(self, ctx:MyJavaParser.InterfaceTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classPermits.
    def visitClassPermits(self, ctx:MyJavaParser.ClassPermitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classBody.
    def visitClassBody(self, ctx:MyJavaParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:MyJavaParser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classMemberDeclaration.
    def visitClassMemberDeclaration(self, ctx:MyJavaParser.ClassMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:MyJavaParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#fieldModifier.
    def visitFieldModifier(self, ctx:MyJavaParser.FieldModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableDeclaratorList.
    def visitVariableDeclaratorList(self, ctx:MyJavaParser.VariableDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:MyJavaParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:MyJavaParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableInitializer.
    def visitVariableInitializer(self, ctx:MyJavaParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unannType.
    def visitUnannType(self, ctx:MyJavaParser.UnannTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unannPrimitiveType.
    def visitUnannPrimitiveType(self, ctx:MyJavaParser.UnannPrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unannReferenceType.
    def visitUnannReferenceType(self, ctx:MyJavaParser.UnannReferenceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unannClassOrInterfaceType.
    def visitUnannClassOrInterfaceType(self, ctx:MyJavaParser.UnannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#uCOIT.
    def visitUCOIT(self, ctx:MyJavaParser.UCOITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unannClassType.
    def visitUnannClassType(self, ctx:MyJavaParser.UnannClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unannInterfaceType.
    def visitUnannInterfaceType(self, ctx:MyJavaParser.UnannInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unannTypeVariable.
    def visitUnannTypeVariable(self, ctx:MyJavaParser.UnannTypeVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unannArrayType.
    def visitUnannArrayType(self, ctx:MyJavaParser.UnannArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MyJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodModifier.
    def visitMethodModifier(self, ctx:MyJavaParser.MethodModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodHeader.
    def visitMethodHeader(self, ctx:MyJavaParser.MethodHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#result.
    def visitResult(self, ctx:MyJavaParser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodDeclarator.
    def visitMethodDeclarator(self, ctx:MyJavaParser.MethodDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#receiverParameter.
    def visitReceiverParameter(self, ctx:MyJavaParser.ReceiverParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#formalParameterList.
    def visitFormalParameterList(self, ctx:MyJavaParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#formalParameter.
    def visitFormalParameter(self, ctx:MyJavaParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableArityParameter.
    def visitVariableArityParameter(self, ctx:MyJavaParser.VariableArityParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableModifier.
    def visitVariableModifier(self, ctx:MyJavaParser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#throwsT.
    def visitThrowsT(self, ctx:MyJavaParser.ThrowsTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#exceptionTypeList.
    def visitExceptionTypeList(self, ctx:MyJavaParser.ExceptionTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#exceptionType.
    def visitExceptionType(self, ctx:MyJavaParser.ExceptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodBody.
    def visitMethodBody(self, ctx:MyJavaParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#instanceInitializer.
    def visitInstanceInitializer(self, ctx:MyJavaParser.InstanceInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#staticInitializer.
    def visitStaticInitializer(self, ctx:MyJavaParser.StaticInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:MyJavaParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#constructorModifier.
    def visitConstructorModifier(self, ctx:MyJavaParser.ConstructorModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#constructorDeclarator.
    def visitConstructorDeclarator(self, ctx:MyJavaParser.ConstructorDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#simpleTypeName.
    def visitSimpleTypeName(self, ctx:MyJavaParser.SimpleTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#constructorBody.
    def visitConstructorBody(self, ctx:MyJavaParser.ConstructorBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#explicitConstructorInvocation.
    def visitExplicitConstructorInvocation(self, ctx:MyJavaParser.ExplicitConstructorInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:MyJavaParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#enumBody.
    def visitEnumBody(self, ctx:MyJavaParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#enumConstantList.
    def visitEnumConstantList(self, ctx:MyJavaParser.EnumConstantListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#enumConstant.
    def visitEnumConstant(self, ctx:MyJavaParser.EnumConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#enumConstantModifier.
    def visitEnumConstantModifier(self, ctx:MyJavaParser.EnumConstantModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#enumBodyDeclarations.
    def visitEnumBodyDeclarations(self, ctx:MyJavaParser.EnumBodyDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#recordDeclaration.
    def visitRecordDeclaration(self, ctx:MyJavaParser.RecordDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#recordHeader.
    def visitRecordHeader(self, ctx:MyJavaParser.RecordHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#recordComponentList.
    def visitRecordComponentList(self, ctx:MyJavaParser.RecordComponentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#recordComponent.
    def visitRecordComponent(self, ctx:MyJavaParser.RecordComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableArityRecordComponent.
    def visitVariableArityRecordComponent(self, ctx:MyJavaParser.VariableArityRecordComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#recordComponentModifier.
    def visitRecordComponentModifier(self, ctx:MyJavaParser.RecordComponentModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#recordBody.
    def visitRecordBody(self, ctx:MyJavaParser.RecordBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#recordBodyDeclaration.
    def visitRecordBodyDeclaration(self, ctx:MyJavaParser.RecordBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#compactConstructorDeclaration.
    def visitCompactConstructorDeclaration(self, ctx:MyJavaParser.CompactConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:MyJavaParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#normalInterfaceDeclaration.
    def visitNormalInterfaceDeclaration(self, ctx:MyJavaParser.NormalInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceModifier.
    def visitInterfaceModifier(self, ctx:MyJavaParser.InterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceExtends.
    def visitInterfaceExtends(self, ctx:MyJavaParser.InterfaceExtendsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfacePermits.
    def visitInterfacePermits(self, ctx:MyJavaParser.InterfacePermitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceBody.
    def visitInterfaceBody(self, ctx:MyJavaParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceMemberDeclaration.
    def visitInterfaceMemberDeclaration(self, ctx:MyJavaParser.InterfaceMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:MyJavaParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#constantModifier.
    def visitConstantModifier(self, ctx:MyJavaParser.ConstantModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceMethodDeclaration.
    def visitInterfaceMethodDeclaration(self, ctx:MyJavaParser.InterfaceMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#interfaceMethodModifier.
    def visitInterfaceMethodModifier(self, ctx:MyJavaParser.InterfaceMethodModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#annotationInterfaceDeclaration.
    def visitAnnotationInterfaceDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#annotationInterfaceBody.
    def visitAnnotationInterfaceBody(self, ctx:MyJavaParser.AnnotationInterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#annotationInterfaceMemberDeclaration.
    def visitAnnotationInterfaceMemberDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#annotationInterfaceElementDeclaration.
    def visitAnnotationInterfaceElementDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceElementDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#annotationInterfaceElementModifier.
    def visitAnnotationInterfaceElementModifier(self, ctx:MyJavaParser.AnnotationInterfaceElementModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#defaultValue.
    def visitDefaultValue(self, ctx:MyJavaParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#annotation.
    def visitAnnotation(self, ctx:MyJavaParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#normalAnnotation.
    def visitNormalAnnotation(self, ctx:MyJavaParser.NormalAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#elementValuePairList.
    def visitElementValuePairList(self, ctx:MyJavaParser.ElementValuePairListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#elementValuePair.
    def visitElementValuePair(self, ctx:MyJavaParser.ElementValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#elementValue.
    def visitElementValue(self, ctx:MyJavaParser.ElementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#elementValueArrayInitializer.
    def visitElementValueArrayInitializer(self, ctx:MyJavaParser.ElementValueArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#elementValueList.
    def visitElementValueList(self, ctx:MyJavaParser.ElementValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#markerAnnotation.
    def visitMarkerAnnotation(self, ctx:MyJavaParser.MarkerAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#singleElementAnnotation.
    def visitSingleElementAnnotation(self, ctx:MyJavaParser.SingleElementAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:MyJavaParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableInitializerList.
    def visitVariableInitializerList(self, ctx:MyJavaParser.VariableInitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#block.
    def visitBlock(self, ctx:MyJavaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#blockStatements.
    def visitBlockStatements(self, ctx:MyJavaParser.BlockStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#blockStatement.
    def visitBlockStatement(self, ctx:MyJavaParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#localClassOrInterfaceDeclaration.
    def visitLocalClassOrInterfaceDeclaration(self, ctx:MyJavaParser.LocalClassOrInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:MyJavaParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#localVariableType.
    def visitLocalVariableType(self, ctx:MyJavaParser.LocalVariableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#localVariableDeclarationStatement.
    def visitLocalVariableDeclarationStatement(self, ctx:MyJavaParser.LocalVariableDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#statement.
    def visitStatement(self, ctx:MyJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#statementNoShortIf.
    def visitStatementNoShortIf(self, ctx:MyJavaParser.StatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#statementWithoutTrailingSubstatement.
    def visitStatementWithoutTrailingSubstatement(self, ctx:MyJavaParser.StatementWithoutTrailingSubstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#emptyStatement_.
    def visitEmptyStatement_(self, ctx:MyJavaParser.EmptyStatement_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#labeledStatement.
    def visitLabeledStatement(self, ctx:MyJavaParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#labeledStatementNoShortIf.
    def visitLabeledStatementNoShortIf(self, ctx:MyJavaParser.LabeledStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MyJavaParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#statementExpression.
    def visitStatementExpression(self, ctx:MyJavaParser.StatementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#ifThenStatement.
    def visitIfThenStatement(self, ctx:MyJavaParser.IfThenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#ifThenElseStatement.
    def visitIfThenElseStatement(self, ctx:MyJavaParser.IfThenElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#ifThenElseStatementNoShortIf.
    def visitIfThenElseStatementNoShortIf(self, ctx:MyJavaParser.IfThenElseStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#assertStatement.
    def visitAssertStatement(self, ctx:MyJavaParser.AssertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchStatement.
    def visitSwitchStatement(self, ctx:MyJavaParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchBlock.
    def visitSwitchBlock(self, ctx:MyJavaParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchRule.
    def visitSwitchRule(self, ctx:MyJavaParser.SwitchRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:MyJavaParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchLabel.
    def visitSwitchLabel(self, ctx:MyJavaParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#caseConstant.
    def visitCaseConstant(self, ctx:MyJavaParser.CaseConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#whileStatement.
    def visitWhileStatement(self, ctx:MyJavaParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#whileStatementNoShortIf.
    def visitWhileStatementNoShortIf(self, ctx:MyJavaParser.WhileStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#doStatement.
    def visitDoStatement(self, ctx:MyJavaParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forStatement.
    def visitForStatement(self, ctx:MyJavaParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forStatementNoShortIf.
    def visitForStatementNoShortIf(self, ctx:MyJavaParser.ForStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#basicForStatement.
    def visitBasicForStatement(self, ctx:MyJavaParser.BasicForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#basicForStatementNoShortIf.
    def visitBasicForStatementNoShortIf(self, ctx:MyJavaParser.BasicForStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forInit.
    def visitForInit(self, ctx:MyJavaParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#forUpdate.
    def visitForUpdate(self, ctx:MyJavaParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#statementExpressionList.
    def visitStatementExpressionList(self, ctx:MyJavaParser.StatementExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#enhancedForStatement.
    def visitEnhancedForStatement(self, ctx:MyJavaParser.EnhancedForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#enhancedForStatementNoShortIf.
    def visitEnhancedForStatementNoShortIf(self, ctx:MyJavaParser.EnhancedForStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#breakStatement.
    def visitBreakStatement(self, ctx:MyJavaParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#continueStatement.
    def visitContinueStatement(self, ctx:MyJavaParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#returnStatement.
    def visitReturnStatement(self, ctx:MyJavaParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#throwStatement.
    def visitThrowStatement(self, ctx:MyJavaParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#synchronizedStatement.
    def visitSynchronizedStatement(self, ctx:MyJavaParser.SynchronizedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#tryStatement.
    def visitTryStatement(self, ctx:MyJavaParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#catches.
    def visitCatches(self, ctx:MyJavaParser.CatchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#catchClause.
    def visitCatchClause(self, ctx:MyJavaParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#catchFormalParameter.
    def visitCatchFormalParameter(self, ctx:MyJavaParser.CatchFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#catchType.
    def visitCatchType(self, ctx:MyJavaParser.CatchTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#finallyBlock.
    def visitFinallyBlock(self, ctx:MyJavaParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#tryWithResourcesStatement.
    def visitTryWithResourcesStatement(self, ctx:MyJavaParser.TryWithResourcesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#resourceSpecification.
    def visitResourceSpecification(self, ctx:MyJavaParser.ResourceSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#resourceList.
    def visitResourceList(self, ctx:MyJavaParser.ResourceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#resource.
    def visitResource(self, ctx:MyJavaParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#variableAccess.
    def visitVariableAccess(self, ctx:MyJavaParser.VariableAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#yieldStatement.
    def visitYieldStatement(self, ctx:MyJavaParser.YieldStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#pattern.
    def visitPattern(self, ctx:MyJavaParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typePattern.
    def visitTypePattern(self, ctx:MyJavaParser.TypePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#expression.
    def visitExpression(self, ctx:MyJavaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#primary.
    def visitPrimary(self, ctx:MyJavaParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#primaryNoNewArray.
    def visitPrimaryNoNewArray(self, ctx:MyJavaParser.PrimaryNoNewArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#pNNA.
    def visitPNNA(self, ctx:MyJavaParser.PNNAContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classLiteral.
    def visitClassLiteral(self, ctx:MyJavaParser.ClassLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classInstanceCreationExpression.
    def visitClassInstanceCreationExpression(self, ctx:MyJavaParser.ClassInstanceCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unqualifiedClassInstanceCreationExpression.
    def visitUnqualifiedClassInstanceCreationExpression(self, ctx:MyJavaParser.UnqualifiedClassInstanceCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#classOrInterfaceTypeToInstantiate.
    def visitClassOrInterfaceTypeToInstantiate(self, ctx:MyJavaParser.ClassOrInterfaceTypeToInstantiateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#typeArgumentsOrDiamond.
    def visitTypeArgumentsOrDiamond(self, ctx:MyJavaParser.TypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#arrayCreationExpression.
    def visitArrayCreationExpression(self, ctx:MyJavaParser.ArrayCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#arrayCreationExpressionWithoutInitializer.
    def visitArrayCreationExpressionWithoutInitializer(self, ctx:MyJavaParser.ArrayCreationExpressionWithoutInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#arrayCreationExpressionWithInitializer.
    def visitArrayCreationExpressionWithInitializer(self, ctx:MyJavaParser.ArrayCreationExpressionWithInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#dimExprs.
    def visitDimExprs(self, ctx:MyJavaParser.DimExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#dimExpr.
    def visitDimExpr(self, ctx:MyJavaParser.DimExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#arrayAccess.
    def visitArrayAccess(self, ctx:MyJavaParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#fieldAccess.
    def visitFieldAccess(self, ctx:MyJavaParser.FieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodInvocation.
    def visitMethodInvocation(self, ctx:MyJavaParser.MethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#argumentList.
    def visitArgumentList(self, ctx:MyJavaParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#methodReference.
    def visitMethodReference(self, ctx:MyJavaParser.MethodReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#postfixExpression.
    def visitPostfixExpression(self, ctx:MyJavaParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#pfE.
    def visitPfE(self, ctx:MyJavaParser.PfEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#postIncrementExpression.
    def visitPostIncrementExpression(self, ctx:MyJavaParser.PostIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#postDecrementExpression.
    def visitPostDecrementExpression(self, ctx:MyJavaParser.PostDecrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MyJavaParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#preIncrementExpression.
    def visitPreIncrementExpression(self, ctx:MyJavaParser.PreIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#preDecrementExpression.
    def visitPreDecrementExpression(self, ctx:MyJavaParser.PreDecrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#unaryExpressionNotPlusMinus.
    def visitUnaryExpressionNotPlusMinus(self, ctx:MyJavaParser.UnaryExpressionNotPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#castExpression.
    def visitCastExpression(self, ctx:MyJavaParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MyJavaParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MyJavaParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#shiftExpression.
    def visitShiftExpression(self, ctx:MyJavaParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#relationalExpression.
    def visitRelationalExpression(self, ctx:MyJavaParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#equalityExpression.
    def visitEqualityExpression(self, ctx:MyJavaParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#andExpression.
    def visitAndExpression(self, ctx:MyJavaParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:MyJavaParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:MyJavaParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#conditionalAndExpression.
    def visitConditionalAndExpression(self, ctx:MyJavaParser.ConditionalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#conditionalOrExpression.
    def visitConditionalOrExpression(self, ctx:MyJavaParser.ConditionalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:MyJavaParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MyJavaParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#assignment.
    def visitAssignment(self, ctx:MyJavaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#leftHandSide.
    def visitLeftHandSide(self, ctx:MyJavaParser.LeftHandSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:MyJavaParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx:MyJavaParser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#lambdaParameters.
    def visitLambdaParameters(self, ctx:MyJavaParser.LambdaParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#lambdaParameterList.
    def visitLambdaParameterList(self, ctx:MyJavaParser.LambdaParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#lambdaParameter.
    def visitLambdaParameter(self, ctx:MyJavaParser.LambdaParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#lambdaParameterType.
    def visitLambdaParameterType(self, ctx:MyJavaParser.LambdaParameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#lambdaBody.
    def visitLambdaBody(self, ctx:MyJavaParser.LambdaBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#switchExpression.
    def visitSwitchExpression(self, ctx:MyJavaParser.SwitchExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyJavaParser#constantExpression.
    def visitConstantExpression(self, ctx:MyJavaParser.ConstantExpressionContext):
        return self.visitChildren(ctx)



del MyJavaParser