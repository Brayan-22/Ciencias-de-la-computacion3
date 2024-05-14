# Generated from Java.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .JavaParser import JavaParser
else:
    from JavaParser import JavaParser

# This class defines a complete listener for a parse tree produced by JavaParser.
class JavaListener(ParseTreeListener):

    # Enter a parse tree produced by JavaParser#compilationUnit.
    def enterCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by JavaParser#compilationUnit.
    def exitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by JavaParser#importDeclaration.
    def enterImportDeclaration(self, ctx:JavaParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#importDeclaration.
    def exitImportDeclaration(self, ctx:JavaParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:JavaParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:JavaParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:JavaParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:JavaParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#classOrInterfaceDeclaration.
    def enterClassOrInterfaceDeclaration(self, ctx:JavaParser.ClassOrInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#classOrInterfaceDeclaration.
    def exitClassOrInterfaceDeclaration(self, ctx:JavaParser.ClassOrInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#classOrInterfaceModifiers.
    def enterClassOrInterfaceModifiers(self, ctx:JavaParser.ClassOrInterfaceModifiersContext):
        pass

    # Exit a parse tree produced by JavaParser#classOrInterfaceModifiers.
    def exitClassOrInterfaceModifiers(self, ctx:JavaParser.ClassOrInterfaceModifiersContext):
        pass


    # Enter a parse tree produced by JavaParser#classOrInterfaceModifier.
    def enterClassOrInterfaceModifier(self, ctx:JavaParser.ClassOrInterfaceModifierContext):
        pass

    # Exit a parse tree produced by JavaParser#classOrInterfaceModifier.
    def exitClassOrInterfaceModifier(self, ctx:JavaParser.ClassOrInterfaceModifierContext):
        pass


    # Enter a parse tree produced by JavaParser#modifiers.
    def enterModifiers(self, ctx:JavaParser.ModifiersContext):
        pass

    # Exit a parse tree produced by JavaParser#modifiers.
    def exitModifiers(self, ctx:JavaParser.ModifiersContext):
        pass


    # Enter a parse tree produced by JavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#normalClassDeclaration.
    def enterNormalClassDeclaration(self, ctx:JavaParser.NormalClassDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#normalClassDeclaration.
    def exitNormalClassDeclaration(self, ctx:JavaParser.NormalClassDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#typeParameters.
    def enterTypeParameters(self, ctx:JavaParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by JavaParser#typeParameters.
    def exitTypeParameters(self, ctx:JavaParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by JavaParser#typeParameter.
    def enterTypeParameter(self, ctx:JavaParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by JavaParser#typeParameter.
    def exitTypeParameter(self, ctx:JavaParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by JavaParser#typeBound.
    def enterTypeBound(self, ctx:JavaParser.TypeBoundContext):
        pass

    # Exit a parse tree produced by JavaParser#typeBound.
    def exitTypeBound(self, ctx:JavaParser.TypeBoundContext):
        pass


    # Enter a parse tree produced by JavaParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:JavaParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:JavaParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#enumBody.
    def enterEnumBody(self, ctx:JavaParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by JavaParser#enumBody.
    def exitEnumBody(self, ctx:JavaParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by JavaParser#enumConstants.
    def enterEnumConstants(self, ctx:JavaParser.EnumConstantsContext):
        pass

    # Exit a parse tree produced by JavaParser#enumConstants.
    def exitEnumConstants(self, ctx:JavaParser.EnumConstantsContext):
        pass


    # Enter a parse tree produced by JavaParser#enumConstant.
    def enterEnumConstant(self, ctx:JavaParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by JavaParser#enumConstant.
    def exitEnumConstant(self, ctx:JavaParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by JavaParser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:JavaParser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by JavaParser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:JavaParser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by JavaParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#normalInterfaceDeclaration.
    def enterNormalInterfaceDeclaration(self, ctx:JavaParser.NormalInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#normalInterfaceDeclaration.
    def exitNormalInterfaceDeclaration(self, ctx:JavaParser.NormalInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#typeList.
    def enterTypeList(self, ctx:JavaParser.TypeListContext):
        pass

    # Exit a parse tree produced by JavaParser#typeList.
    def exitTypeList(self, ctx:JavaParser.TypeListContext):
        pass


    # Enter a parse tree produced by JavaParser#classBody.
    def enterClassBody(self, ctx:JavaParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by JavaParser#classBody.
    def exitClassBody(self, ctx:JavaParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by JavaParser#interfaceBody.
    def enterInterfaceBody(self, ctx:JavaParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by JavaParser#interfaceBody.
    def exitInterfaceBody(self, ctx:JavaParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by JavaParser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:JavaParser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:JavaParser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#memberDecl.
    def enterMemberDecl(self, ctx:JavaParser.MemberDeclContext):
        pass

    # Exit a parse tree produced by JavaParser#memberDecl.
    def exitMemberDecl(self, ctx:JavaParser.MemberDeclContext):
        pass


    # Enter a parse tree produced by JavaParser#mainMethod.
    def enterMainMethod(self, ctx:JavaParser.MainMethodContext):
        pass

    # Exit a parse tree produced by JavaParser#mainMethod.
    def exitMainMethod(self, ctx:JavaParser.MainMethodContext):
        pass


    # Enter a parse tree produced by JavaParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:JavaParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:JavaParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#genericMethodOrConstructorDecl.
    def enterGenericMethodOrConstructorDecl(self, ctx:JavaParser.GenericMethodOrConstructorDeclContext):
        pass

    # Exit a parse tree produced by JavaParser#genericMethodOrConstructorDecl.
    def exitGenericMethodOrConstructorDecl(self, ctx:JavaParser.GenericMethodOrConstructorDeclContext):
        pass


    # Enter a parse tree produced by JavaParser#genericMethodOrConstructorRest.
    def enterGenericMethodOrConstructorRest(self, ctx:JavaParser.GenericMethodOrConstructorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#genericMethodOrConstructorRest.
    def exitGenericMethodOrConstructorRest(self, ctx:JavaParser.GenericMethodOrConstructorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#interfaceBodyDeclaration.
    def enterInterfaceBodyDeclaration(self, ctx:JavaParser.InterfaceBodyDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#interfaceBodyDeclaration.
    def exitInterfaceBodyDeclaration(self, ctx:JavaParser.InterfaceBodyDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#interfaceMemberDecl.
    def enterInterfaceMemberDecl(self, ctx:JavaParser.InterfaceMemberDeclContext):
        pass

    # Exit a parse tree produced by JavaParser#interfaceMemberDecl.
    def exitInterfaceMemberDecl(self, ctx:JavaParser.InterfaceMemberDeclContext):
        pass


    # Enter a parse tree produced by JavaParser#interfaceMethodOrFieldDecl.
    def enterInterfaceMethodOrFieldDecl(self, ctx:JavaParser.InterfaceMethodOrFieldDeclContext):
        pass

    # Exit a parse tree produced by JavaParser#interfaceMethodOrFieldDecl.
    def exitInterfaceMethodOrFieldDecl(self, ctx:JavaParser.InterfaceMethodOrFieldDeclContext):
        pass


    # Enter a parse tree produced by JavaParser#interfaceMethodOrFieldRest.
    def enterInterfaceMethodOrFieldRest(self, ctx:JavaParser.InterfaceMethodOrFieldRestContext):
        pass

    # Exit a parse tree produced by JavaParser#interfaceMethodOrFieldRest.
    def exitInterfaceMethodOrFieldRest(self, ctx:JavaParser.InterfaceMethodOrFieldRestContext):
        pass


    # Enter a parse tree produced by JavaParser#methodDeclaratorRest.
    def enterMethodDeclaratorRest(self, ctx:JavaParser.MethodDeclaratorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#methodDeclaratorRest.
    def exitMethodDeclaratorRest(self, ctx:JavaParser.MethodDeclaratorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#voidMethodDeclaratorRest.
    def enterVoidMethodDeclaratorRest(self, ctx:JavaParser.VoidMethodDeclaratorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#voidMethodDeclaratorRest.
    def exitVoidMethodDeclaratorRest(self, ctx:JavaParser.VoidMethodDeclaratorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#interfaceMethodDeclaratorRest.
    def enterInterfaceMethodDeclaratorRest(self, ctx:JavaParser.InterfaceMethodDeclaratorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#interfaceMethodDeclaratorRest.
    def exitInterfaceMethodDeclaratorRest(self, ctx:JavaParser.InterfaceMethodDeclaratorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#interfaceGenericMethodDecl.
    def enterInterfaceGenericMethodDecl(self, ctx:JavaParser.InterfaceGenericMethodDeclContext):
        pass

    # Exit a parse tree produced by JavaParser#interfaceGenericMethodDecl.
    def exitInterfaceGenericMethodDecl(self, ctx:JavaParser.InterfaceGenericMethodDeclContext):
        pass


    # Enter a parse tree produced by JavaParser#voidInterfaceMethodDeclaratorRest.
    def enterVoidInterfaceMethodDeclaratorRest(self, ctx:JavaParser.VoidInterfaceMethodDeclaratorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#voidInterfaceMethodDeclaratorRest.
    def exitVoidInterfaceMethodDeclaratorRest(self, ctx:JavaParser.VoidInterfaceMethodDeclaratorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#constructorDeclaratorRest.
    def enterConstructorDeclaratorRest(self, ctx:JavaParser.ConstructorDeclaratorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#constructorDeclaratorRest.
    def exitConstructorDeclaratorRest(self, ctx:JavaParser.ConstructorDeclaratorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#constantDeclarator.
    def enterConstantDeclarator(self, ctx:JavaParser.ConstantDeclaratorContext):
        pass

    # Exit a parse tree produced by JavaParser#constantDeclarator.
    def exitConstantDeclarator(self, ctx:JavaParser.ConstantDeclaratorContext):
        pass


    # Enter a parse tree produced by JavaParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:JavaParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by JavaParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:JavaParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by JavaParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by JavaParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by JavaParser#constantDeclaratorsRest.
    def enterConstantDeclaratorsRest(self, ctx:JavaParser.ConstantDeclaratorsRestContext):
        pass

    # Exit a parse tree produced by JavaParser#constantDeclaratorsRest.
    def exitConstantDeclaratorsRest(self, ctx:JavaParser.ConstantDeclaratorsRestContext):
        pass


    # Enter a parse tree produced by JavaParser#constantDeclaratorRest.
    def enterConstantDeclaratorRest(self, ctx:JavaParser.ConstantDeclaratorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#constantDeclaratorRest.
    def exitConstantDeclaratorRest(self, ctx:JavaParser.ConstantDeclaratorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:JavaParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by JavaParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:JavaParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by JavaParser#variableInitializer.
    def enterVariableInitializer(self, ctx:JavaParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by JavaParser#variableInitializer.
    def exitVariableInitializer(self, ctx:JavaParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by JavaParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:JavaParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by JavaParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:JavaParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by JavaParser#modifier.
    def enterModifier(self, ctx:JavaParser.ModifierContext):
        pass

    # Exit a parse tree produced by JavaParser#modifier.
    def exitModifier(self, ctx:JavaParser.ModifierContext):
        pass


    # Enter a parse tree produced by JavaParser#packageOrTypeName.
    def enterPackageOrTypeName(self, ctx:JavaParser.PackageOrTypeNameContext):
        pass

    # Exit a parse tree produced by JavaParser#packageOrTypeName.
    def exitPackageOrTypeName(self, ctx:JavaParser.PackageOrTypeNameContext):
        pass


    # Enter a parse tree produced by JavaParser#enumConstantName.
    def enterEnumConstantName(self, ctx:JavaParser.EnumConstantNameContext):
        pass

    # Exit a parse tree produced by JavaParser#enumConstantName.
    def exitEnumConstantName(self, ctx:JavaParser.EnumConstantNameContext):
        pass


    # Enter a parse tree produced by JavaParser#typeName.
    def enterTypeName(self, ctx:JavaParser.TypeNameContext):
        pass

    # Exit a parse tree produced by JavaParser#typeName.
    def exitTypeName(self, ctx:JavaParser.TypeNameContext):
        pass


    # Enter a parse tree produced by JavaParser#type.
    def enterType(self, ctx:JavaParser.TypeContext):
        pass

    # Exit a parse tree produced by JavaParser#type.
    def exitType(self, ctx:JavaParser.TypeContext):
        pass


    # Enter a parse tree produced by JavaParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:JavaParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by JavaParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:JavaParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by JavaParser#primitiveType.
    def enterPrimitiveType(self, ctx:JavaParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by JavaParser#primitiveType.
    def exitPrimitiveType(self, ctx:JavaParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by JavaParser#variableModifier.
    def enterVariableModifier(self, ctx:JavaParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by JavaParser#variableModifier.
    def exitVariableModifier(self, ctx:JavaParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by JavaParser#typeArguments.
    def enterTypeArguments(self, ctx:JavaParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by JavaParser#typeArguments.
    def exitTypeArguments(self, ctx:JavaParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by JavaParser#typeArgument.
    def enterTypeArgument(self, ctx:JavaParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by JavaParser#typeArgument.
    def exitTypeArgument(self, ctx:JavaParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by JavaParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:JavaParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by JavaParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:JavaParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by JavaParser#formalParameters.
    def enterFormalParameters(self, ctx:JavaParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by JavaParser#formalParameters.
    def exitFormalParameters(self, ctx:JavaParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by JavaParser#formalParameterDecls.
    def enterFormalParameterDecls(self, ctx:JavaParser.FormalParameterDeclsContext):
        pass

    # Exit a parse tree produced by JavaParser#formalParameterDecls.
    def exitFormalParameterDecls(self, ctx:JavaParser.FormalParameterDeclsContext):
        pass


    # Enter a parse tree produced by JavaParser#formalParameterDeclsRest.
    def enterFormalParameterDeclsRest(self, ctx:JavaParser.FormalParameterDeclsRestContext):
        pass

    # Exit a parse tree produced by JavaParser#formalParameterDeclsRest.
    def exitFormalParameterDeclsRest(self, ctx:JavaParser.FormalParameterDeclsRestContext):
        pass


    # Enter a parse tree produced by JavaParser#methodBody.
    def enterMethodBody(self, ctx:JavaParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by JavaParser#methodBody.
    def exitMethodBody(self, ctx:JavaParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by JavaParser#constructorBody.
    def enterConstructorBody(self, ctx:JavaParser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by JavaParser#constructorBody.
    def exitConstructorBody(self, ctx:JavaParser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by JavaParser#qualifiedName.
    def enterQualifiedName(self, ctx:JavaParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by JavaParser#qualifiedName.
    def exitQualifiedName(self, ctx:JavaParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by JavaParser#literal.
    def enterLiteral(self, ctx:JavaParser.LiteralContext):
        pass

    # Exit a parse tree produced by JavaParser#literal.
    def exitLiteral(self, ctx:JavaParser.LiteralContext):
        pass


    # Enter a parse tree produced by JavaParser#annotations.
    def enterAnnotations(self, ctx:JavaParser.AnnotationsContext):
        pass

    # Exit a parse tree produced by JavaParser#annotations.
    def exitAnnotations(self, ctx:JavaParser.AnnotationsContext):
        pass


    # Enter a parse tree produced by JavaParser#annotation.
    def enterAnnotation(self, ctx:JavaParser.AnnotationContext):
        pass

    # Exit a parse tree produced by JavaParser#annotation.
    def exitAnnotation(self, ctx:JavaParser.AnnotationContext):
        pass


    # Enter a parse tree produced by JavaParser#annotationName.
    def enterAnnotationName(self, ctx:JavaParser.AnnotationNameContext):
        pass

    # Exit a parse tree produced by JavaParser#annotationName.
    def exitAnnotationName(self, ctx:JavaParser.AnnotationNameContext):
        pass


    # Enter a parse tree produced by JavaParser#elementValuePairs.
    def enterElementValuePairs(self, ctx:JavaParser.ElementValuePairsContext):
        pass

    # Exit a parse tree produced by JavaParser#elementValuePairs.
    def exitElementValuePairs(self, ctx:JavaParser.ElementValuePairsContext):
        pass


    # Enter a parse tree produced by JavaParser#elementValuePair.
    def enterElementValuePair(self, ctx:JavaParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by JavaParser#elementValuePair.
    def exitElementValuePair(self, ctx:JavaParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by JavaParser#elementValue.
    def enterElementValue(self, ctx:JavaParser.ElementValueContext):
        pass

    # Exit a parse tree produced by JavaParser#elementValue.
    def exitElementValue(self, ctx:JavaParser.ElementValueContext):
        pass


    # Enter a parse tree produced by JavaParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:JavaParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by JavaParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:JavaParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by JavaParser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:JavaParser.AnnotationTypeDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#annotationTypeDeclaration.
    def exitAnnotationTypeDeclaration(self, ctx:JavaParser.AnnotationTypeDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:JavaParser.AnnotationTypeBodyContext):
        pass

    # Exit a parse tree produced by JavaParser#annotationTypeBody.
    def exitAnnotationTypeBody(self, ctx:JavaParser.AnnotationTypeBodyContext):
        pass


    # Enter a parse tree produced by JavaParser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:JavaParser.AnnotationTypeElementDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#annotationTypeElementDeclaration.
    def exitAnnotationTypeElementDeclaration(self, ctx:JavaParser.AnnotationTypeElementDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#annotationTypeElementRest.
    def enterAnnotationTypeElementRest(self, ctx:JavaParser.AnnotationTypeElementRestContext):
        pass

    # Exit a parse tree produced by JavaParser#annotationTypeElementRest.
    def exitAnnotationTypeElementRest(self, ctx:JavaParser.AnnotationTypeElementRestContext):
        pass


    # Enter a parse tree produced by JavaParser#annotationMethodOrConstantRest.
    def enterAnnotationMethodOrConstantRest(self, ctx:JavaParser.AnnotationMethodOrConstantRestContext):
        pass

    # Exit a parse tree produced by JavaParser#annotationMethodOrConstantRest.
    def exitAnnotationMethodOrConstantRest(self, ctx:JavaParser.AnnotationMethodOrConstantRestContext):
        pass


    # Enter a parse tree produced by JavaParser#annotationMethodRest.
    def enterAnnotationMethodRest(self, ctx:JavaParser.AnnotationMethodRestContext):
        pass

    # Exit a parse tree produced by JavaParser#annotationMethodRest.
    def exitAnnotationMethodRest(self, ctx:JavaParser.AnnotationMethodRestContext):
        pass


    # Enter a parse tree produced by JavaParser#annotationConstantRest.
    def enterAnnotationConstantRest(self, ctx:JavaParser.AnnotationConstantRestContext):
        pass

    # Exit a parse tree produced by JavaParser#annotationConstantRest.
    def exitAnnotationConstantRest(self, ctx:JavaParser.AnnotationConstantRestContext):
        pass


    # Enter a parse tree produced by JavaParser#defaultValue.
    def enterDefaultValue(self, ctx:JavaParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by JavaParser#defaultValue.
    def exitDefaultValue(self, ctx:JavaParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by JavaParser#block.
    def enterBlock(self, ctx:JavaParser.BlockContext):
        pass

    # Exit a parse tree produced by JavaParser#block.
    def exitBlock(self, ctx:JavaParser.BlockContext):
        pass


    # Enter a parse tree produced by JavaParser#blockStatement.
    def enterBlockStatement(self, ctx:JavaParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by JavaParser#blockStatement.
    def exitBlockStatement(self, ctx:JavaParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by JavaParser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:JavaParser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by JavaParser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:JavaParser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by JavaParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by JavaParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by JavaParser#variableModifiers.
    def enterVariableModifiers(self, ctx:JavaParser.VariableModifiersContext):
        pass

    # Exit a parse tree produced by JavaParser#variableModifiers.
    def exitVariableModifiers(self, ctx:JavaParser.VariableModifiersContext):
        pass


    # Enter a parse tree produced by JavaParser#statement.
    def enterStatement(self, ctx:JavaParser.StatementContext):
        pass

    # Exit a parse tree produced by JavaParser#statement.
    def exitStatement(self, ctx:JavaParser.StatementContext):
        pass


    # Enter a parse tree produced by JavaParser#catches.
    def enterCatches(self, ctx:JavaParser.CatchesContext):
        pass

    # Exit a parse tree produced by JavaParser#catches.
    def exitCatches(self, ctx:JavaParser.CatchesContext):
        pass


    # Enter a parse tree produced by JavaParser#catchClause.
    def enterCatchClause(self, ctx:JavaParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by JavaParser#catchClause.
    def exitCatchClause(self, ctx:JavaParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by JavaParser#catchType.
    def enterCatchType(self, ctx:JavaParser.CatchTypeContext):
        pass

    # Exit a parse tree produced by JavaParser#catchType.
    def exitCatchType(self, ctx:JavaParser.CatchTypeContext):
        pass


    # Enter a parse tree produced by JavaParser#finallyBlock.
    def enterFinallyBlock(self, ctx:JavaParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by JavaParser#finallyBlock.
    def exitFinallyBlock(self, ctx:JavaParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by JavaParser#resourceSpecification.
    def enterResourceSpecification(self, ctx:JavaParser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by JavaParser#resourceSpecification.
    def exitResourceSpecification(self, ctx:JavaParser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by JavaParser#resources.
    def enterResources(self, ctx:JavaParser.ResourcesContext):
        pass

    # Exit a parse tree produced by JavaParser#resources.
    def exitResources(self, ctx:JavaParser.ResourcesContext):
        pass


    # Enter a parse tree produced by JavaParser#resource.
    def enterResource(self, ctx:JavaParser.ResourceContext):
        pass

    # Exit a parse tree produced by JavaParser#resource.
    def exitResource(self, ctx:JavaParser.ResourceContext):
        pass


    # Enter a parse tree produced by JavaParser#formalParameter.
    def enterFormalParameter(self, ctx:JavaParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by JavaParser#formalParameter.
    def exitFormalParameter(self, ctx:JavaParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by JavaParser#switchBlockStatementGroups.
    def enterSwitchBlockStatementGroups(self, ctx:JavaParser.SwitchBlockStatementGroupsContext):
        pass

    # Exit a parse tree produced by JavaParser#switchBlockStatementGroups.
    def exitSwitchBlockStatementGroups(self, ctx:JavaParser.SwitchBlockStatementGroupsContext):
        pass


    # Enter a parse tree produced by JavaParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:JavaParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by JavaParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:JavaParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by JavaParser#switchLabel.
    def enterSwitchLabel(self, ctx:JavaParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by JavaParser#switchLabel.
    def exitSwitchLabel(self, ctx:JavaParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by JavaParser#forControl.
    def enterForControl(self, ctx:JavaParser.ForControlContext):
        pass

    # Exit a parse tree produced by JavaParser#forControl.
    def exitForControl(self, ctx:JavaParser.ForControlContext):
        pass


    # Enter a parse tree produced by JavaParser#forInit.
    def enterForInit(self, ctx:JavaParser.ForInitContext):
        pass

    # Exit a parse tree produced by JavaParser#forInit.
    def exitForInit(self, ctx:JavaParser.ForInitContext):
        pass


    # Enter a parse tree produced by JavaParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:JavaParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by JavaParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:JavaParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by JavaParser#forUpdate.
    def enterForUpdate(self, ctx:JavaParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by JavaParser#forUpdate.
    def exitForUpdate(self, ctx:JavaParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by JavaParser#parExpression.
    def enterParExpression(self, ctx:JavaParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#parExpression.
    def exitParExpression(self, ctx:JavaParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#expressionList.
    def enterExpressionList(self, ctx:JavaParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by JavaParser#expressionList.
    def exitExpressionList(self, ctx:JavaParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by JavaParser#statementExpression.
    def enterStatementExpression(self, ctx:JavaParser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#statementExpression.
    def exitStatementExpression(self, ctx:JavaParser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#constantExpression.
    def enterConstantExpression(self, ctx:JavaParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#constantExpression.
    def exitConstantExpression(self, ctx:JavaParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#expression.
    def enterExpression(self, ctx:JavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#expression.
    def exitExpression(self, ctx:JavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:JavaParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by JavaParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:JavaParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by JavaParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:JavaParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:JavaParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:JavaParser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx:JavaParser.ConditionalOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:JavaParser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:JavaParser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:JavaParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:JavaParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:JavaParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:JavaParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#andExpression.
    def enterAndExpression(self, ctx:JavaParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#andExpression.
    def exitAndExpression(self, ctx:JavaParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#equalityExpression.
    def enterEqualityExpression(self, ctx:JavaParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#equalityExpression.
    def exitEqualityExpression(self, ctx:JavaParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#instanceOfExpression.
    def enterInstanceOfExpression(self, ctx:JavaParser.InstanceOfExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#instanceOfExpression.
    def exitInstanceOfExpression(self, ctx:JavaParser.InstanceOfExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#relationalExpression.
    def enterRelationalExpression(self, ctx:JavaParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#relationalExpression.
    def exitRelationalExpression(self, ctx:JavaParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#relationalOp.
    def enterRelationalOp(self, ctx:JavaParser.RelationalOpContext):
        pass

    # Exit a parse tree produced by JavaParser#relationalOp.
    def exitRelationalOp(self, ctx:JavaParser.RelationalOpContext):
        pass


    # Enter a parse tree produced by JavaParser#shiftExpression.
    def enterShiftExpression(self, ctx:JavaParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#shiftExpression.
    def exitShiftExpression(self, ctx:JavaParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#shiftOp.
    def enterShiftOp(self, ctx:JavaParser.ShiftOpContext):
        pass

    # Exit a parse tree produced by JavaParser#shiftOp.
    def exitShiftOp(self, ctx:JavaParser.ShiftOpContext):
        pass


    # Enter a parse tree produced by JavaParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:JavaParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:JavaParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:JavaParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:JavaParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#unaryExpression.
    def enterUnaryExpression(self, ctx:JavaParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#unaryExpression.
    def exitUnaryExpression(self, ctx:JavaParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#unaryExpressionNotPlusMinus.
    def enterUnaryExpressionNotPlusMinus(self, ctx:JavaParser.UnaryExpressionNotPlusMinusContext):
        pass

    # Exit a parse tree produced by JavaParser#unaryExpressionNotPlusMinus.
    def exitUnaryExpressionNotPlusMinus(self, ctx:JavaParser.UnaryExpressionNotPlusMinusContext):
        pass


    # Enter a parse tree produced by JavaParser#castExpression.
    def enterCastExpression(self, ctx:JavaParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by JavaParser#castExpression.
    def exitCastExpression(self, ctx:JavaParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by JavaParser#primary.
    def enterPrimary(self, ctx:JavaParser.PrimaryContext):
        pass

    # Exit a parse tree produced by JavaParser#primary.
    def exitPrimary(self, ctx:JavaParser.PrimaryContext):
        pass


    # Enter a parse tree produced by JavaParser#identifierSuffix.
    def enterIdentifierSuffix(self, ctx:JavaParser.IdentifierSuffixContext):
        pass

    # Exit a parse tree produced by JavaParser#identifierSuffix.
    def exitIdentifierSuffix(self, ctx:JavaParser.IdentifierSuffixContext):
        pass


    # Enter a parse tree produced by JavaParser#creator.
    def enterCreator(self, ctx:JavaParser.CreatorContext):
        pass

    # Exit a parse tree produced by JavaParser#creator.
    def exitCreator(self, ctx:JavaParser.CreatorContext):
        pass


    # Enter a parse tree produced by JavaParser#createdName.
    def enterCreatedName(self, ctx:JavaParser.CreatedNameContext):
        pass

    # Exit a parse tree produced by JavaParser#createdName.
    def exitCreatedName(self, ctx:JavaParser.CreatedNameContext):
        pass


    # Enter a parse tree produced by JavaParser#innerCreator.
    def enterInnerCreator(self, ctx:JavaParser.InnerCreatorContext):
        pass

    # Exit a parse tree produced by JavaParser#innerCreator.
    def exitInnerCreator(self, ctx:JavaParser.InnerCreatorContext):
        pass


    # Enter a parse tree produced by JavaParser#arrayCreatorRest.
    def enterArrayCreatorRest(self, ctx:JavaParser.ArrayCreatorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#arrayCreatorRest.
    def exitArrayCreatorRest(self, ctx:JavaParser.ArrayCreatorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#classCreatorRest.
    def enterClassCreatorRest(self, ctx:JavaParser.ClassCreatorRestContext):
        pass

    # Exit a parse tree produced by JavaParser#classCreatorRest.
    def exitClassCreatorRest(self, ctx:JavaParser.ClassCreatorRestContext):
        pass


    # Enter a parse tree produced by JavaParser#explicitGenericInvocation.
    def enterExplicitGenericInvocation(self, ctx:JavaParser.ExplicitGenericInvocationContext):
        pass

    # Exit a parse tree produced by JavaParser#explicitGenericInvocation.
    def exitExplicitGenericInvocation(self, ctx:JavaParser.ExplicitGenericInvocationContext):
        pass


    # Enter a parse tree produced by JavaParser#nonWildcardTypeArguments.
    def enterNonWildcardTypeArguments(self, ctx:JavaParser.NonWildcardTypeArgumentsContext):
        pass

    # Exit a parse tree produced by JavaParser#nonWildcardTypeArguments.
    def exitNonWildcardTypeArguments(self, ctx:JavaParser.NonWildcardTypeArgumentsContext):
        pass


    # Enter a parse tree produced by JavaParser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:JavaParser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by JavaParser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:JavaParser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by JavaParser#nonWildcardTypeArgumentsOrDiamond.
    def enterNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by JavaParser#nonWildcardTypeArgumentsOrDiamond.
    def exitNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by JavaParser#selector.
    def enterSelector(self, ctx:JavaParser.SelectorContext):
        pass

    # Exit a parse tree produced by JavaParser#selector.
    def exitSelector(self, ctx:JavaParser.SelectorContext):
        pass


    # Enter a parse tree produced by JavaParser#superSuffix.
    def enterSuperSuffix(self, ctx:JavaParser.SuperSuffixContext):
        pass

    # Exit a parse tree produced by JavaParser#superSuffix.
    def exitSuperSuffix(self, ctx:JavaParser.SuperSuffixContext):
        pass


    # Enter a parse tree produced by JavaParser#explicitGenericInvocationSuffix.
    def enterExplicitGenericInvocationSuffix(self, ctx:JavaParser.ExplicitGenericInvocationSuffixContext):
        pass

    # Exit a parse tree produced by JavaParser#explicitGenericInvocationSuffix.
    def exitExplicitGenericInvocationSuffix(self, ctx:JavaParser.ExplicitGenericInvocationSuffixContext):
        pass


    # Enter a parse tree produced by JavaParser#arguments.
    def enterArguments(self, ctx:JavaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by JavaParser#arguments.
    def exitArguments(self, ctx:JavaParser.ArgumentsContext):
        pass



del JavaParser