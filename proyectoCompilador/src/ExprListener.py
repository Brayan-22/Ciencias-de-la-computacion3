# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#compilationUnit.
    def enterCompilationUnit(self, ctx:ExprParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by ExprParser#compilationUnit.
    def exitCompilationUnit(self, ctx:ExprParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by ExprParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:ExprParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:ExprParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:ExprParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:ExprParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#classOrInterfaceDeclaration.
    def enterClassOrInterfaceDeclaration(self, ctx:ExprParser.ClassOrInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#classOrInterfaceDeclaration.
    def exitClassOrInterfaceDeclaration(self, ctx:ExprParser.ClassOrInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#classOrInterfaceModifiers.
    def enterClassOrInterfaceModifiers(self, ctx:ExprParser.ClassOrInterfaceModifiersContext):
        pass

    # Exit a parse tree produced by ExprParser#classOrInterfaceModifiers.
    def exitClassOrInterfaceModifiers(self, ctx:ExprParser.ClassOrInterfaceModifiersContext):
        pass


    # Enter a parse tree produced by ExprParser#classOrInterfaceModifier.
    def enterClassOrInterfaceModifier(self, ctx:ExprParser.ClassOrInterfaceModifierContext):
        pass

    # Exit a parse tree produced by ExprParser#classOrInterfaceModifier.
    def exitClassOrInterfaceModifier(self, ctx:ExprParser.ClassOrInterfaceModifierContext):
        pass


    # Enter a parse tree produced by ExprParser#modifiers.
    def enterModifiers(self, ctx:ExprParser.ModifiersContext):
        pass

    # Exit a parse tree produced by ExprParser#modifiers.
    def exitModifiers(self, ctx:ExprParser.ModifiersContext):
        pass


    # Enter a parse tree produced by ExprParser#classDeclaration.
    def enterClassDeclaration(self, ctx:ExprParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#classDeclaration.
    def exitClassDeclaration(self, ctx:ExprParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#normalClassDeclaration.
    def enterNormalClassDeclaration(self, ctx:ExprParser.NormalClassDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#normalClassDeclaration.
    def exitNormalClassDeclaration(self, ctx:ExprParser.NormalClassDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#typeParameters.
    def enterTypeParameters(self, ctx:ExprParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by ExprParser#typeParameters.
    def exitTypeParameters(self, ctx:ExprParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by ExprParser#typeParameter.
    def enterTypeParameter(self, ctx:ExprParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by ExprParser#typeParameter.
    def exitTypeParameter(self, ctx:ExprParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by ExprParser#typeBound.
    def enterTypeBound(self, ctx:ExprParser.TypeBoundContext):
        pass

    # Exit a parse tree produced by ExprParser#typeBound.
    def exitTypeBound(self, ctx:ExprParser.TypeBoundContext):
        pass


    # Enter a parse tree produced by ExprParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:ExprParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:ExprParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#enumBody.
    def enterEnumBody(self, ctx:ExprParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by ExprParser#enumBody.
    def exitEnumBody(self, ctx:ExprParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by ExprParser#enumConstants.
    def enterEnumConstants(self, ctx:ExprParser.EnumConstantsContext):
        pass

    # Exit a parse tree produced by ExprParser#enumConstants.
    def exitEnumConstants(self, ctx:ExprParser.EnumConstantsContext):
        pass


    # Enter a parse tree produced by ExprParser#enumConstant.
    def enterEnumConstant(self, ctx:ExprParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by ExprParser#enumConstant.
    def exitEnumConstant(self, ctx:ExprParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by ExprParser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:ExprParser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by ExprParser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:ExprParser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:ExprParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:ExprParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#normalInterfaceDeclaration.
    def enterNormalInterfaceDeclaration(self, ctx:ExprParser.NormalInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#normalInterfaceDeclaration.
    def exitNormalInterfaceDeclaration(self, ctx:ExprParser.NormalInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#typeList.
    def enterTypeList(self, ctx:ExprParser.TypeListContext):
        pass

    # Exit a parse tree produced by ExprParser#typeList.
    def exitTypeList(self, ctx:ExprParser.TypeListContext):
        pass


    # Enter a parse tree produced by ExprParser#classBody.
    def enterClassBody(self, ctx:ExprParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by ExprParser#classBody.
    def exitClassBody(self, ctx:ExprParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceBody.
    def enterInterfaceBody(self, ctx:ExprParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceBody.
    def exitInterfaceBody(self, ctx:ExprParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by ExprParser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:ExprParser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:ExprParser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#memberDecl.
    def enterMemberDecl(self, ctx:ExprParser.MemberDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#memberDecl.
    def exitMemberDecl(self, ctx:ExprParser.MemberDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:ExprParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:ExprParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#genericMethodOrConstructorDecl.
    def enterGenericMethodOrConstructorDecl(self, ctx:ExprParser.GenericMethodOrConstructorDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#genericMethodOrConstructorDecl.
    def exitGenericMethodOrConstructorDecl(self, ctx:ExprParser.GenericMethodOrConstructorDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#genericMethodOrConstructorRest.
    def enterGenericMethodOrConstructorRest(self, ctx:ExprParser.GenericMethodOrConstructorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#genericMethodOrConstructorRest.
    def exitGenericMethodOrConstructorRest(self, ctx:ExprParser.GenericMethodOrConstructorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:ExprParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:ExprParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:ExprParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:ExprParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceBodyDeclaration.
    def enterInterfaceBodyDeclaration(self, ctx:ExprParser.InterfaceBodyDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceBodyDeclaration.
    def exitInterfaceBodyDeclaration(self, ctx:ExprParser.InterfaceBodyDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceMemberDecl.
    def enterInterfaceMemberDecl(self, ctx:ExprParser.InterfaceMemberDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceMemberDecl.
    def exitInterfaceMemberDecl(self, ctx:ExprParser.InterfaceMemberDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceMethodOrFieldDecl.
    def enterInterfaceMethodOrFieldDecl(self, ctx:ExprParser.InterfaceMethodOrFieldDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceMethodOrFieldDecl.
    def exitInterfaceMethodOrFieldDecl(self, ctx:ExprParser.InterfaceMethodOrFieldDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceMethodOrFieldRest.
    def enterInterfaceMethodOrFieldRest(self, ctx:ExprParser.InterfaceMethodOrFieldRestContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceMethodOrFieldRest.
    def exitInterfaceMethodOrFieldRest(self, ctx:ExprParser.InterfaceMethodOrFieldRestContext):
        pass


    # Enter a parse tree produced by ExprParser#methodDeclaratorRest.
    def enterMethodDeclaratorRest(self, ctx:ExprParser.MethodDeclaratorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#methodDeclaratorRest.
    def exitMethodDeclaratorRest(self, ctx:ExprParser.MethodDeclaratorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#voidMethodDeclaratorRest.
    def enterVoidMethodDeclaratorRest(self, ctx:ExprParser.VoidMethodDeclaratorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#voidMethodDeclaratorRest.
    def exitVoidMethodDeclaratorRest(self, ctx:ExprParser.VoidMethodDeclaratorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceMethodDeclaratorRest.
    def enterInterfaceMethodDeclaratorRest(self, ctx:ExprParser.InterfaceMethodDeclaratorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceMethodDeclaratorRest.
    def exitInterfaceMethodDeclaratorRest(self, ctx:ExprParser.InterfaceMethodDeclaratorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceGenericMethodDecl.
    def enterInterfaceGenericMethodDecl(self, ctx:ExprParser.InterfaceGenericMethodDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceGenericMethodDecl.
    def exitInterfaceGenericMethodDecl(self, ctx:ExprParser.InterfaceGenericMethodDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#voidInterfaceMethodDeclaratorRest.
    def enterVoidInterfaceMethodDeclaratorRest(self, ctx:ExprParser.VoidInterfaceMethodDeclaratorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#voidInterfaceMethodDeclaratorRest.
    def exitVoidInterfaceMethodDeclaratorRest(self, ctx:ExprParser.VoidInterfaceMethodDeclaratorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#constructorDeclaratorRest.
    def enterConstructorDeclaratorRest(self, ctx:ExprParser.ConstructorDeclaratorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#constructorDeclaratorRest.
    def exitConstructorDeclaratorRest(self, ctx:ExprParser.ConstructorDeclaratorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#constantDeclarator.
    def enterConstantDeclarator(self, ctx:ExprParser.ConstantDeclaratorContext):
        pass

    # Exit a parse tree produced by ExprParser#constantDeclarator.
    def exitConstantDeclarator(self, ctx:ExprParser.ConstantDeclaratorContext):
        pass


    # Enter a parse tree produced by ExprParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:ExprParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by ExprParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:ExprParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by ExprParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:ExprParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by ExprParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:ExprParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by ExprParser#constantDeclaratorsRest.
    def enterConstantDeclaratorsRest(self, ctx:ExprParser.ConstantDeclaratorsRestContext):
        pass

    # Exit a parse tree produced by ExprParser#constantDeclaratorsRest.
    def exitConstantDeclaratorsRest(self, ctx:ExprParser.ConstantDeclaratorsRestContext):
        pass


    # Enter a parse tree produced by ExprParser#constantDeclaratorRest.
    def enterConstantDeclaratorRest(self, ctx:ExprParser.ConstantDeclaratorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#constantDeclaratorRest.
    def exitConstantDeclaratorRest(self, ctx:ExprParser.ConstantDeclaratorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:ExprParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by ExprParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:ExprParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by ExprParser#variableInitializer.
    def enterVariableInitializer(self, ctx:ExprParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by ExprParser#variableInitializer.
    def exitVariableInitializer(self, ctx:ExprParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by ExprParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:ExprParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:ExprParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by ExprParser#modifier.
    def enterModifier(self, ctx:ExprParser.ModifierContext):
        pass

    # Exit a parse tree produced by ExprParser#modifier.
    def exitModifier(self, ctx:ExprParser.ModifierContext):
        pass


    # Enter a parse tree produced by ExprParser#packageOrTypeName.
    def enterPackageOrTypeName(self, ctx:ExprParser.PackageOrTypeNameContext):
        pass

    # Exit a parse tree produced by ExprParser#packageOrTypeName.
    def exitPackageOrTypeName(self, ctx:ExprParser.PackageOrTypeNameContext):
        pass


    # Enter a parse tree produced by ExprParser#enumConstantName.
    def enterEnumConstantName(self, ctx:ExprParser.EnumConstantNameContext):
        pass

    # Exit a parse tree produced by ExprParser#enumConstantName.
    def exitEnumConstantName(self, ctx:ExprParser.EnumConstantNameContext):
        pass


    # Enter a parse tree produced by ExprParser#typeName.
    def enterTypeName(self, ctx:ExprParser.TypeNameContext):
        pass

    # Exit a parse tree produced by ExprParser#typeName.
    def exitTypeName(self, ctx:ExprParser.TypeNameContext):
        pass


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


    # Enter a parse tree produced by ExprParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:ExprParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:ExprParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#primitiveType.
    def enterPrimitiveType(self, ctx:ExprParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#primitiveType.
    def exitPrimitiveType(self, ctx:ExprParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#variableModifier.
    def enterVariableModifier(self, ctx:ExprParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by ExprParser#variableModifier.
    def exitVariableModifier(self, ctx:ExprParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by ExprParser#typeArguments.
    def enterTypeArguments(self, ctx:ExprParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by ExprParser#typeArguments.
    def exitTypeArguments(self, ctx:ExprParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by ExprParser#typeArgument.
    def enterTypeArgument(self, ctx:ExprParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by ExprParser#typeArgument.
    def exitTypeArgument(self, ctx:ExprParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by ExprParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:ExprParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by ExprParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:ExprParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by ExprParser#formalParameters.
    def enterFormalParameters(self, ctx:ExprParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by ExprParser#formalParameters.
    def exitFormalParameters(self, ctx:ExprParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by ExprParser#formalParameterDecls.
    def enterFormalParameterDecls(self, ctx:ExprParser.FormalParameterDeclsContext):
        pass

    # Exit a parse tree produced by ExprParser#formalParameterDecls.
    def exitFormalParameterDecls(self, ctx:ExprParser.FormalParameterDeclsContext):
        pass


    # Enter a parse tree produced by ExprParser#formalParameterDeclsRest.
    def enterFormalParameterDeclsRest(self, ctx:ExprParser.FormalParameterDeclsRestContext):
        pass

    # Exit a parse tree produced by ExprParser#formalParameterDeclsRest.
    def exitFormalParameterDeclsRest(self, ctx:ExprParser.FormalParameterDeclsRestContext):
        pass


    # Enter a parse tree produced by ExprParser#methodBody.
    def enterMethodBody(self, ctx:ExprParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by ExprParser#methodBody.
    def exitMethodBody(self, ctx:ExprParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by ExprParser#constructorBody.
    def enterConstructorBody(self, ctx:ExprParser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by ExprParser#constructorBody.
    def exitConstructorBody(self, ctx:ExprParser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by ExprParser#qualifiedName.
    def enterQualifiedName(self, ctx:ExprParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by ExprParser#qualifiedName.
    def exitQualifiedName(self, ctx:ExprParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by ExprParser#literal.
    def enterLiteral(self, ctx:ExprParser.LiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#literal.
    def exitLiteral(self, ctx:ExprParser.LiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#annotations.
    def enterAnnotations(self, ctx:ExprParser.AnnotationsContext):
        pass

    # Exit a parse tree produced by ExprParser#annotations.
    def exitAnnotations(self, ctx:ExprParser.AnnotationsContext):
        pass


    # Enter a parse tree produced by ExprParser#annotation.
    def enterAnnotation(self, ctx:ExprParser.AnnotationContext):
        pass

    # Exit a parse tree produced by ExprParser#annotation.
    def exitAnnotation(self, ctx:ExprParser.AnnotationContext):
        pass


    # Enter a parse tree produced by ExprParser#annotationName.
    def enterAnnotationName(self, ctx:ExprParser.AnnotationNameContext):
        pass

    # Exit a parse tree produced by ExprParser#annotationName.
    def exitAnnotationName(self, ctx:ExprParser.AnnotationNameContext):
        pass


    # Enter a parse tree produced by ExprParser#elementValuePairs.
    def enterElementValuePairs(self, ctx:ExprParser.ElementValuePairsContext):
        pass

    # Exit a parse tree produced by ExprParser#elementValuePairs.
    def exitElementValuePairs(self, ctx:ExprParser.ElementValuePairsContext):
        pass


    # Enter a parse tree produced by ExprParser#elementValuePair.
    def enterElementValuePair(self, ctx:ExprParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by ExprParser#elementValuePair.
    def exitElementValuePair(self, ctx:ExprParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by ExprParser#elementValue.
    def enterElementValue(self, ctx:ExprParser.ElementValueContext):
        pass

    # Exit a parse tree produced by ExprParser#elementValue.
    def exitElementValue(self, ctx:ExprParser.ElementValueContext):
        pass


    # Enter a parse tree produced by ExprParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:ExprParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by ExprParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:ExprParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by ExprParser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:ExprParser.AnnotationTypeDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#annotationTypeDeclaration.
    def exitAnnotationTypeDeclaration(self, ctx:ExprParser.AnnotationTypeDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:ExprParser.AnnotationTypeBodyContext):
        pass

    # Exit a parse tree produced by ExprParser#annotationTypeBody.
    def exitAnnotationTypeBody(self, ctx:ExprParser.AnnotationTypeBodyContext):
        pass


    # Enter a parse tree produced by ExprParser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:ExprParser.AnnotationTypeElementDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#annotationTypeElementDeclaration.
    def exitAnnotationTypeElementDeclaration(self, ctx:ExprParser.AnnotationTypeElementDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#annotationTypeElementRest.
    def enterAnnotationTypeElementRest(self, ctx:ExprParser.AnnotationTypeElementRestContext):
        pass

    # Exit a parse tree produced by ExprParser#annotationTypeElementRest.
    def exitAnnotationTypeElementRest(self, ctx:ExprParser.AnnotationTypeElementRestContext):
        pass


    # Enter a parse tree produced by ExprParser#annotationMethodOrConstantRest.
    def enterAnnotationMethodOrConstantRest(self, ctx:ExprParser.AnnotationMethodOrConstantRestContext):
        pass

    # Exit a parse tree produced by ExprParser#annotationMethodOrConstantRest.
    def exitAnnotationMethodOrConstantRest(self, ctx:ExprParser.AnnotationMethodOrConstantRestContext):
        pass


    # Enter a parse tree produced by ExprParser#annotationMethodRest.
    def enterAnnotationMethodRest(self, ctx:ExprParser.AnnotationMethodRestContext):
        pass

    # Exit a parse tree produced by ExprParser#annotationMethodRest.
    def exitAnnotationMethodRest(self, ctx:ExprParser.AnnotationMethodRestContext):
        pass


    # Enter a parse tree produced by ExprParser#annotationConstantRest.
    def enterAnnotationConstantRest(self, ctx:ExprParser.AnnotationConstantRestContext):
        pass

    # Exit a parse tree produced by ExprParser#annotationConstantRest.
    def exitAnnotationConstantRest(self, ctx:ExprParser.AnnotationConstantRestContext):
        pass


    # Enter a parse tree produced by ExprParser#defaultValue.
    def enterDefaultValue(self, ctx:ExprParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by ExprParser#defaultValue.
    def exitDefaultValue(self, ctx:ExprParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#blockStatement.
    def enterBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#blockStatement.
    def exitBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:ExprParser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:ExprParser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:ExprParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:ExprParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#variableModifiers.
    def enterVariableModifiers(self, ctx:ExprParser.VariableModifiersContext):
        pass

    # Exit a parse tree produced by ExprParser#variableModifiers.
    def exitVariableModifiers(self, ctx:ExprParser.VariableModifiersContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#catches.
    def enterCatches(self, ctx:ExprParser.CatchesContext):
        pass

    # Exit a parse tree produced by ExprParser#catches.
    def exitCatches(self, ctx:ExprParser.CatchesContext):
        pass


    # Enter a parse tree produced by ExprParser#catchClause.
    def enterCatchClause(self, ctx:ExprParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by ExprParser#catchClause.
    def exitCatchClause(self, ctx:ExprParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by ExprParser#catchType.
    def enterCatchType(self, ctx:ExprParser.CatchTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#catchType.
    def exitCatchType(self, ctx:ExprParser.CatchTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#finallyBlock.
    def enterFinallyBlock(self, ctx:ExprParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#finallyBlock.
    def exitFinallyBlock(self, ctx:ExprParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by ExprParser#resourceSpecification.
    def enterResourceSpecification(self, ctx:ExprParser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by ExprParser#resourceSpecification.
    def exitResourceSpecification(self, ctx:ExprParser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by ExprParser#resources.
    def enterResources(self, ctx:ExprParser.ResourcesContext):
        pass

    # Exit a parse tree produced by ExprParser#resources.
    def exitResources(self, ctx:ExprParser.ResourcesContext):
        pass


    # Enter a parse tree produced by ExprParser#resource.
    def enterResource(self, ctx:ExprParser.ResourceContext):
        pass

    # Exit a parse tree produced by ExprParser#resource.
    def exitResource(self, ctx:ExprParser.ResourceContext):
        pass


    # Enter a parse tree produced by ExprParser#formalParameter.
    def enterFormalParameter(self, ctx:ExprParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by ExprParser#formalParameter.
    def exitFormalParameter(self, ctx:ExprParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by ExprParser#switchBlockStatementGroups.
    def enterSwitchBlockStatementGroups(self, ctx:ExprParser.SwitchBlockStatementGroupsContext):
        pass

    # Exit a parse tree produced by ExprParser#switchBlockStatementGroups.
    def exitSwitchBlockStatementGroups(self, ctx:ExprParser.SwitchBlockStatementGroupsContext):
        pass


    # Enter a parse tree produced by ExprParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:ExprParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by ExprParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:ExprParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by ExprParser#switchLabel.
    def enterSwitchLabel(self, ctx:ExprParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by ExprParser#switchLabel.
    def exitSwitchLabel(self, ctx:ExprParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by ExprParser#forControl.
    def enterForControl(self, ctx:ExprParser.ForControlContext):
        pass

    # Exit a parse tree produced by ExprParser#forControl.
    def exitForControl(self, ctx:ExprParser.ForControlContext):
        pass


    # Enter a parse tree produced by ExprParser#forInit.
    def enterForInit(self, ctx:ExprParser.ForInitContext):
        pass

    # Exit a parse tree produced by ExprParser#forInit.
    def exitForInit(self, ctx:ExprParser.ForInitContext):
        pass


    # Enter a parse tree produced by ExprParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:ExprParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by ExprParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:ExprParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by ExprParser#forUpdate.
    def enterForUpdate(self, ctx:ExprParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by ExprParser#forUpdate.
    def exitForUpdate(self, ctx:ExprParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by ExprParser#parExpression.
    def enterParExpression(self, ctx:ExprParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#parExpression.
    def exitParExpression(self, ctx:ExprParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#expressionList.
    def enterExpressionList(self, ctx:ExprParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by ExprParser#expressionList.
    def exitExpressionList(self, ctx:ExprParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by ExprParser#statementExpression.
    def enterStatementExpression(self, ctx:ExprParser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#statementExpression.
    def exitStatementExpression(self, ctx:ExprParser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#constantExpression.
    def enterConstantExpression(self, ctx:ExprParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#constantExpression.
    def exitConstantExpression(self, ctx:ExprParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:ExprParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by ExprParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:ExprParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by ExprParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:ExprParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:ExprParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:ExprParser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx:ExprParser.ConditionalOrExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:ExprParser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:ExprParser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:ExprParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:ExprParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:ExprParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:ExprParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#andExpression.
    def enterAndExpression(self, ctx:ExprParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#andExpression.
    def exitAndExpression(self, ctx:ExprParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#equalityExpression.
    def enterEqualityExpression(self, ctx:ExprParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#equalityExpression.
    def exitEqualityExpression(self, ctx:ExprParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#instanceOfExpression.
    def enterInstanceOfExpression(self, ctx:ExprParser.InstanceOfExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#instanceOfExpression.
    def exitInstanceOfExpression(self, ctx:ExprParser.InstanceOfExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#relationalExpression.
    def enterRelationalExpression(self, ctx:ExprParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#relationalExpression.
    def exitRelationalExpression(self, ctx:ExprParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#relationalOp.
    def enterRelationalOp(self, ctx:ExprParser.RelationalOpContext):
        pass

    # Exit a parse tree produced by ExprParser#relationalOp.
    def exitRelationalOp(self, ctx:ExprParser.RelationalOpContext):
        pass


    # Enter a parse tree produced by ExprParser#shiftExpression.
    def enterShiftExpression(self, ctx:ExprParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#shiftExpression.
    def exitShiftExpression(self, ctx:ExprParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#shiftOp.
    def enterShiftOp(self, ctx:ExprParser.ShiftOpContext):
        pass

    # Exit a parse tree produced by ExprParser#shiftOp.
    def exitShiftOp(self, ctx:ExprParser.ShiftOpContext):
        pass


    # Enter a parse tree produced by ExprParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:ExprParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:ExprParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:ExprParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:ExprParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#unaryExpression.
    def enterUnaryExpression(self, ctx:ExprParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#unaryExpression.
    def exitUnaryExpression(self, ctx:ExprParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#unaryExpressionNotPlusMinus.
    def enterUnaryExpressionNotPlusMinus(self, ctx:ExprParser.UnaryExpressionNotPlusMinusContext):
        pass

    # Exit a parse tree produced by ExprParser#unaryExpressionNotPlusMinus.
    def exitUnaryExpressionNotPlusMinus(self, ctx:ExprParser.UnaryExpressionNotPlusMinusContext):
        pass


    # Enter a parse tree produced by ExprParser#castExpression.
    def enterCastExpression(self, ctx:ExprParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#castExpression.
    def exitCastExpression(self, ctx:ExprParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#primary.
    def enterPrimary(self, ctx:ExprParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ExprParser#primary.
    def exitPrimary(self, ctx:ExprParser.PrimaryContext):
        pass


    # Enter a parse tree produced by ExprParser#identifierSuffix.
    def enterIdentifierSuffix(self, ctx:ExprParser.IdentifierSuffixContext):
        pass

    # Exit a parse tree produced by ExprParser#identifierSuffix.
    def exitIdentifierSuffix(self, ctx:ExprParser.IdentifierSuffixContext):
        pass


    # Enter a parse tree produced by ExprParser#creator.
    def enterCreator(self, ctx:ExprParser.CreatorContext):
        pass

    # Exit a parse tree produced by ExprParser#creator.
    def exitCreator(self, ctx:ExprParser.CreatorContext):
        pass


    # Enter a parse tree produced by ExprParser#createdName.
    def enterCreatedName(self, ctx:ExprParser.CreatedNameContext):
        pass

    # Exit a parse tree produced by ExprParser#createdName.
    def exitCreatedName(self, ctx:ExprParser.CreatedNameContext):
        pass


    # Enter a parse tree produced by ExprParser#innerCreator.
    def enterInnerCreator(self, ctx:ExprParser.InnerCreatorContext):
        pass

    # Exit a parse tree produced by ExprParser#innerCreator.
    def exitInnerCreator(self, ctx:ExprParser.InnerCreatorContext):
        pass


    # Enter a parse tree produced by ExprParser#arrayCreatorRest.
    def enterArrayCreatorRest(self, ctx:ExprParser.ArrayCreatorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayCreatorRest.
    def exitArrayCreatorRest(self, ctx:ExprParser.ArrayCreatorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#classCreatorRest.
    def enterClassCreatorRest(self, ctx:ExprParser.ClassCreatorRestContext):
        pass

    # Exit a parse tree produced by ExprParser#classCreatorRest.
    def exitClassCreatorRest(self, ctx:ExprParser.ClassCreatorRestContext):
        pass


    # Enter a parse tree produced by ExprParser#explicitGenericInvocation.
    def enterExplicitGenericInvocation(self, ctx:ExprParser.ExplicitGenericInvocationContext):
        pass

    # Exit a parse tree produced by ExprParser#explicitGenericInvocation.
    def exitExplicitGenericInvocation(self, ctx:ExprParser.ExplicitGenericInvocationContext):
        pass


    # Enter a parse tree produced by ExprParser#nonWildcardTypeArguments.
    def enterNonWildcardTypeArguments(self, ctx:ExprParser.NonWildcardTypeArgumentsContext):
        pass

    # Exit a parse tree produced by ExprParser#nonWildcardTypeArguments.
    def exitNonWildcardTypeArguments(self, ctx:ExprParser.NonWildcardTypeArgumentsContext):
        pass


    # Enter a parse tree produced by ExprParser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:ExprParser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by ExprParser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:ExprParser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by ExprParser#nonWildcardTypeArgumentsOrDiamond.
    def enterNonWildcardTypeArgumentsOrDiamond(self, ctx:ExprParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by ExprParser#nonWildcardTypeArgumentsOrDiamond.
    def exitNonWildcardTypeArgumentsOrDiamond(self, ctx:ExprParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by ExprParser#selector.
    def enterSelector(self, ctx:ExprParser.SelectorContext):
        pass

    # Exit a parse tree produced by ExprParser#selector.
    def exitSelector(self, ctx:ExprParser.SelectorContext):
        pass


    # Enter a parse tree produced by ExprParser#superSuffix.
    def enterSuperSuffix(self, ctx:ExprParser.SuperSuffixContext):
        pass

    # Exit a parse tree produced by ExprParser#superSuffix.
    def exitSuperSuffix(self, ctx:ExprParser.SuperSuffixContext):
        pass


    # Enter a parse tree produced by ExprParser#explicitGenericInvocationSuffix.
    def enterExplicitGenericInvocationSuffix(self, ctx:ExprParser.ExplicitGenericInvocationSuffixContext):
        pass

    # Exit a parse tree produced by ExprParser#explicitGenericInvocationSuffix.
    def exitExplicitGenericInvocationSuffix(self, ctx:ExprParser.ExplicitGenericInvocationSuffixContext):
        pass


    # Enter a parse tree produced by ExprParser#arguments.
    def enterArguments(self, ctx:ExprParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by ExprParser#arguments.
    def exitArguments(self, ctx:ExprParser.ArgumentsContext):
        pass



del ExprParser