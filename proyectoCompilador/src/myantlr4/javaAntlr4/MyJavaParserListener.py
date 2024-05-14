# Generated from MyJavaParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyJavaParser import MyJavaParser
else:
    from MyJavaParser import MyJavaParser

# This class defines a complete listener for a parse tree produced by MyJavaParser.
class MyJavaParserListener(ParseTreeListener):

    # Enter a parse tree produced by MyJavaParser#start_.
    def enterStart_(self, ctx:MyJavaParser.Start_Context):
        pass

    # Exit a parse tree produced by MyJavaParser#start_.
    def exitStart_(self, ctx:MyJavaParser.Start_Context):
        pass


    # Enter a parse tree produced by MyJavaParser#literal.
    def enterLiteral(self, ctx:MyJavaParser.LiteralContext):
        pass

    # Exit a parse tree produced by MyJavaParser#literal.
    def exitLiteral(self, ctx:MyJavaParser.LiteralContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeIdentifier.
    def enterTypeIdentifier(self, ctx:MyJavaParser.TypeIdentifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeIdentifier.
    def exitTypeIdentifier(self, ctx:MyJavaParser.TypeIdentifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unqualifiedMethodIdentifier.
    def enterUnqualifiedMethodIdentifier(self, ctx:MyJavaParser.UnqualifiedMethodIdentifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unqualifiedMethodIdentifier.
    def exitUnqualifiedMethodIdentifier(self, ctx:MyJavaParser.UnqualifiedMethodIdentifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#primitiveType.
    def enterPrimitiveType(self, ctx:MyJavaParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#primitiveType.
    def exitPrimitiveType(self, ctx:MyJavaParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#numericType.
    def enterNumericType(self, ctx:MyJavaParser.NumericTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#numericType.
    def exitNumericType(self, ctx:MyJavaParser.NumericTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#integralType.
    def enterIntegralType(self, ctx:MyJavaParser.IntegralTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#integralType.
    def exitIntegralType(self, ctx:MyJavaParser.IntegralTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#floatingPointType.
    def enterFloatingPointType(self, ctx:MyJavaParser.FloatingPointTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#floatingPointType.
    def exitFloatingPointType(self, ctx:MyJavaParser.FloatingPointTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#referenceType.
    def enterReferenceType(self, ctx:MyJavaParser.ReferenceTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#referenceType.
    def exitReferenceType(self, ctx:MyJavaParser.ReferenceTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#coit.
    def enterCoit(self, ctx:MyJavaParser.CoitContext):
        pass

    # Exit a parse tree produced by MyJavaParser#coit.
    def exitCoit(self, ctx:MyJavaParser.CoitContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:MyJavaParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:MyJavaParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classType.
    def enterClassType(self, ctx:MyJavaParser.ClassTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classType.
    def exitClassType(self, ctx:MyJavaParser.ClassTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceType.
    def enterInterfaceType(self, ctx:MyJavaParser.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceType.
    def exitInterfaceType(self, ctx:MyJavaParser.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeVariable.
    def enterTypeVariable(self, ctx:MyJavaParser.TypeVariableContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeVariable.
    def exitTypeVariable(self, ctx:MyJavaParser.TypeVariableContext):
        pass


    # Enter a parse tree produced by MyJavaParser#arrayType.
    def enterArrayType(self, ctx:MyJavaParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#arrayType.
    def exitArrayType(self, ctx:MyJavaParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#dims.
    def enterDims(self, ctx:MyJavaParser.DimsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#dims.
    def exitDims(self, ctx:MyJavaParser.DimsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeParameter.
    def enterTypeParameter(self, ctx:MyJavaParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeParameter.
    def exitTypeParameter(self, ctx:MyJavaParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeParameterModifier.
    def enterTypeParameterModifier(self, ctx:MyJavaParser.TypeParameterModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeParameterModifier.
    def exitTypeParameterModifier(self, ctx:MyJavaParser.TypeParameterModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeBound.
    def enterTypeBound(self, ctx:MyJavaParser.TypeBoundContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeBound.
    def exitTypeBound(self, ctx:MyJavaParser.TypeBoundContext):
        pass


    # Enter a parse tree produced by MyJavaParser#additionalBound.
    def enterAdditionalBound(self, ctx:MyJavaParser.AdditionalBoundContext):
        pass

    # Exit a parse tree produced by MyJavaParser#additionalBound.
    def exitAdditionalBound(self, ctx:MyJavaParser.AdditionalBoundContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeArguments.
    def enterTypeArguments(self, ctx:MyJavaParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeArguments.
    def exitTypeArguments(self, ctx:MyJavaParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeArgumentList.
    def enterTypeArgumentList(self, ctx:MyJavaParser.TypeArgumentListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeArgumentList.
    def exitTypeArgumentList(self, ctx:MyJavaParser.TypeArgumentListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeArgument.
    def enterTypeArgument(self, ctx:MyJavaParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeArgument.
    def exitTypeArgument(self, ctx:MyJavaParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by MyJavaParser#wildcard.
    def enterWildcard(self, ctx:MyJavaParser.WildcardContext):
        pass

    # Exit a parse tree produced by MyJavaParser#wildcard.
    def exitWildcard(self, ctx:MyJavaParser.WildcardContext):
        pass


    # Enter a parse tree produced by MyJavaParser#wildcardBounds.
    def enterWildcardBounds(self, ctx:MyJavaParser.WildcardBoundsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#wildcardBounds.
    def exitWildcardBounds(self, ctx:MyJavaParser.WildcardBoundsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#moduleName.
    def enterModuleName(self, ctx:MyJavaParser.ModuleNameContext):
        pass

    # Exit a parse tree produced by MyJavaParser#moduleName.
    def exitModuleName(self, ctx:MyJavaParser.ModuleNameContext):
        pass


    # Enter a parse tree produced by MyJavaParser#packageName.
    def enterPackageName(self, ctx:MyJavaParser.PackageNameContext):
        pass

    # Exit a parse tree produced by MyJavaParser#packageName.
    def exitPackageName(self, ctx:MyJavaParser.PackageNameContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeName.
    def enterTypeName(self, ctx:MyJavaParser.TypeNameContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeName.
    def exitTypeName(self, ctx:MyJavaParser.TypeNameContext):
        pass


    # Enter a parse tree produced by MyJavaParser#packageOrTypeName.
    def enterPackageOrTypeName(self, ctx:MyJavaParser.PackageOrTypeNameContext):
        pass

    # Exit a parse tree produced by MyJavaParser#packageOrTypeName.
    def exitPackageOrTypeName(self, ctx:MyJavaParser.PackageOrTypeNameContext):
        pass


    # Enter a parse tree produced by MyJavaParser#expressionName.
    def enterExpressionName(self, ctx:MyJavaParser.ExpressionNameContext):
        pass

    # Exit a parse tree produced by MyJavaParser#expressionName.
    def exitExpressionName(self, ctx:MyJavaParser.ExpressionNameContext):
        pass


    # Enter a parse tree produced by MyJavaParser#methodName.
    def enterMethodName(self, ctx:MyJavaParser.MethodNameContext):
        pass

    # Exit a parse tree produced by MyJavaParser#methodName.
    def exitMethodName(self, ctx:MyJavaParser.MethodNameContext):
        pass


    # Enter a parse tree produced by MyJavaParser#ambiguousName.
    def enterAmbiguousName(self, ctx:MyJavaParser.AmbiguousNameContext):
        pass

    # Exit a parse tree produced by MyJavaParser#ambiguousName.
    def exitAmbiguousName(self, ctx:MyJavaParser.AmbiguousNameContext):
        pass


    # Enter a parse tree produced by MyJavaParser#compilationUnit.
    def enterCompilationUnit(self, ctx:MyJavaParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by MyJavaParser#compilationUnit.
    def exitCompilationUnit(self, ctx:MyJavaParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by MyJavaParser#ordinaryCompilationUnit.
    def enterOrdinaryCompilationUnit(self, ctx:MyJavaParser.OrdinaryCompilationUnitContext):
        pass

    # Exit a parse tree produced by MyJavaParser#ordinaryCompilationUnit.
    def exitOrdinaryCompilationUnit(self, ctx:MyJavaParser.OrdinaryCompilationUnitContext):
        pass


    # Enter a parse tree produced by MyJavaParser#modularCompilationUnit.
    def enterModularCompilationUnit(self, ctx:MyJavaParser.ModularCompilationUnitContext):
        pass

    # Exit a parse tree produced by MyJavaParser#modularCompilationUnit.
    def exitModularCompilationUnit(self, ctx:MyJavaParser.ModularCompilationUnitContext):
        pass


    # Enter a parse tree produced by MyJavaParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:MyJavaParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:MyJavaParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#packageModifier.
    def enterPackageModifier(self, ctx:MyJavaParser.PackageModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#packageModifier.
    def exitPackageModifier(self, ctx:MyJavaParser.PackageModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#importDeclaration.
    def enterImportDeclaration(self, ctx:MyJavaParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#importDeclaration.
    def exitImportDeclaration(self, ctx:MyJavaParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#singleTypeImportDeclaration.
    def enterSingleTypeImportDeclaration(self, ctx:MyJavaParser.SingleTypeImportDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#singleTypeImportDeclaration.
    def exitSingleTypeImportDeclaration(self, ctx:MyJavaParser.SingleTypeImportDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeImportOnDemandDeclaration.
    def enterTypeImportOnDemandDeclaration(self, ctx:MyJavaParser.TypeImportOnDemandDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeImportOnDemandDeclaration.
    def exitTypeImportOnDemandDeclaration(self, ctx:MyJavaParser.TypeImportOnDemandDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#singleStaticImportDeclaration.
    def enterSingleStaticImportDeclaration(self, ctx:MyJavaParser.SingleStaticImportDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#singleStaticImportDeclaration.
    def exitSingleStaticImportDeclaration(self, ctx:MyJavaParser.SingleStaticImportDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#staticImportOnDemandDeclaration.
    def enterStaticImportOnDemandDeclaration(self, ctx:MyJavaParser.StaticImportOnDemandDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#staticImportOnDemandDeclaration.
    def exitStaticImportOnDemandDeclaration(self, ctx:MyJavaParser.StaticImportOnDemandDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#topLevelClassOrInterfaceDeclaration.
    def enterTopLevelClassOrInterfaceDeclaration(self, ctx:MyJavaParser.TopLevelClassOrInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#topLevelClassOrInterfaceDeclaration.
    def exitTopLevelClassOrInterfaceDeclaration(self, ctx:MyJavaParser.TopLevelClassOrInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#moduleDeclaration.
    def enterModuleDeclaration(self, ctx:MyJavaParser.ModuleDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#moduleDeclaration.
    def exitModuleDeclaration(self, ctx:MyJavaParser.ModuleDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#moduleDirective.
    def enterModuleDirective(self, ctx:MyJavaParser.ModuleDirectiveContext):
        pass

    # Exit a parse tree produced by MyJavaParser#moduleDirective.
    def exitModuleDirective(self, ctx:MyJavaParser.ModuleDirectiveContext):
        pass


    # Enter a parse tree produced by MyJavaParser#requiresModifier.
    def enterRequiresModifier(self, ctx:MyJavaParser.RequiresModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#requiresModifier.
    def exitRequiresModifier(self, ctx:MyJavaParser.RequiresModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:MyJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:MyJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#normalClassDeclaration.
    def enterNormalClassDeclaration(self, ctx:MyJavaParser.NormalClassDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#normalClassDeclaration.
    def exitNormalClassDeclaration(self, ctx:MyJavaParser.NormalClassDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classModifier.
    def enterClassModifier(self, ctx:MyJavaParser.ClassModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classModifier.
    def exitClassModifier(self, ctx:MyJavaParser.ClassModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeParameters.
    def enterTypeParameters(self, ctx:MyJavaParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeParameters.
    def exitTypeParameters(self, ctx:MyJavaParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeParameterList.
    def enterTypeParameterList(self, ctx:MyJavaParser.TypeParameterListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeParameterList.
    def exitTypeParameterList(self, ctx:MyJavaParser.TypeParameterListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classExtends.
    def enterClassExtends(self, ctx:MyJavaParser.ClassExtendsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classExtends.
    def exitClassExtends(self, ctx:MyJavaParser.ClassExtendsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classImplements.
    def enterClassImplements(self, ctx:MyJavaParser.ClassImplementsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classImplements.
    def exitClassImplements(self, ctx:MyJavaParser.ClassImplementsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceTypeList.
    def enterInterfaceTypeList(self, ctx:MyJavaParser.InterfaceTypeListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceTypeList.
    def exitInterfaceTypeList(self, ctx:MyJavaParser.InterfaceTypeListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classPermits.
    def enterClassPermits(self, ctx:MyJavaParser.ClassPermitsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classPermits.
    def exitClassPermits(self, ctx:MyJavaParser.ClassPermitsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classBody.
    def enterClassBody(self, ctx:MyJavaParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classBody.
    def exitClassBody(self, ctx:MyJavaParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:MyJavaParser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:MyJavaParser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classMemberDeclaration.
    def enterClassMemberDeclaration(self, ctx:MyJavaParser.ClassMemberDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classMemberDeclaration.
    def exitClassMemberDeclaration(self, ctx:MyJavaParser.ClassMemberDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:MyJavaParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:MyJavaParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#fieldModifier.
    def enterFieldModifier(self, ctx:MyJavaParser.FieldModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#fieldModifier.
    def exitFieldModifier(self, ctx:MyJavaParser.FieldModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableDeclaratorList.
    def enterVariableDeclaratorList(self, ctx:MyJavaParser.VariableDeclaratorListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableDeclaratorList.
    def exitVariableDeclaratorList(self, ctx:MyJavaParser.VariableDeclaratorListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:MyJavaParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:MyJavaParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:MyJavaParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:MyJavaParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableInitializer.
    def enterVariableInitializer(self, ctx:MyJavaParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableInitializer.
    def exitVariableInitializer(self, ctx:MyJavaParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unannType.
    def enterUnannType(self, ctx:MyJavaParser.UnannTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unannType.
    def exitUnannType(self, ctx:MyJavaParser.UnannTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unannPrimitiveType.
    def enterUnannPrimitiveType(self, ctx:MyJavaParser.UnannPrimitiveTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unannPrimitiveType.
    def exitUnannPrimitiveType(self, ctx:MyJavaParser.UnannPrimitiveTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unannReferenceType.
    def enterUnannReferenceType(self, ctx:MyJavaParser.UnannReferenceTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unannReferenceType.
    def exitUnannReferenceType(self, ctx:MyJavaParser.UnannReferenceTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unannClassOrInterfaceType.
    def enterUnannClassOrInterfaceType(self, ctx:MyJavaParser.UnannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unannClassOrInterfaceType.
    def exitUnannClassOrInterfaceType(self, ctx:MyJavaParser.UnannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#uCOIT.
    def enterUCOIT(self, ctx:MyJavaParser.UCOITContext):
        pass

    # Exit a parse tree produced by MyJavaParser#uCOIT.
    def exitUCOIT(self, ctx:MyJavaParser.UCOITContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unannClassType.
    def enterUnannClassType(self, ctx:MyJavaParser.UnannClassTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unannClassType.
    def exitUnannClassType(self, ctx:MyJavaParser.UnannClassTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unannInterfaceType.
    def enterUnannInterfaceType(self, ctx:MyJavaParser.UnannInterfaceTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unannInterfaceType.
    def exitUnannInterfaceType(self, ctx:MyJavaParser.UnannInterfaceTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unannTypeVariable.
    def enterUnannTypeVariable(self, ctx:MyJavaParser.UnannTypeVariableContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unannTypeVariable.
    def exitUnannTypeVariable(self, ctx:MyJavaParser.UnannTypeVariableContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unannArrayType.
    def enterUnannArrayType(self, ctx:MyJavaParser.UnannArrayTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unannArrayType.
    def exitUnannArrayType(self, ctx:MyJavaParser.UnannArrayTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:MyJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:MyJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#methodModifier.
    def enterMethodModifier(self, ctx:MyJavaParser.MethodModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#methodModifier.
    def exitMethodModifier(self, ctx:MyJavaParser.MethodModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#methodHeader.
    def enterMethodHeader(self, ctx:MyJavaParser.MethodHeaderContext):
        pass

    # Exit a parse tree produced by MyJavaParser#methodHeader.
    def exitMethodHeader(self, ctx:MyJavaParser.MethodHeaderContext):
        pass


    # Enter a parse tree produced by MyJavaParser#result.
    def enterResult(self, ctx:MyJavaParser.ResultContext):
        pass

    # Exit a parse tree produced by MyJavaParser#result.
    def exitResult(self, ctx:MyJavaParser.ResultContext):
        pass


    # Enter a parse tree produced by MyJavaParser#methodDeclarator.
    def enterMethodDeclarator(self, ctx:MyJavaParser.MethodDeclaratorContext):
        pass

    # Exit a parse tree produced by MyJavaParser#methodDeclarator.
    def exitMethodDeclarator(self, ctx:MyJavaParser.MethodDeclaratorContext):
        pass


    # Enter a parse tree produced by MyJavaParser#receiverParameter.
    def enterReceiverParameter(self, ctx:MyJavaParser.ReceiverParameterContext):
        pass

    # Exit a parse tree produced by MyJavaParser#receiverParameter.
    def exitReceiverParameter(self, ctx:MyJavaParser.ReceiverParameterContext):
        pass


    # Enter a parse tree produced by MyJavaParser#formalParameterList.
    def enterFormalParameterList(self, ctx:MyJavaParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#formalParameterList.
    def exitFormalParameterList(self, ctx:MyJavaParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#formalParameter.
    def enterFormalParameter(self, ctx:MyJavaParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by MyJavaParser#formalParameter.
    def exitFormalParameter(self, ctx:MyJavaParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableArityParameter.
    def enterVariableArityParameter(self, ctx:MyJavaParser.VariableArityParameterContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableArityParameter.
    def exitVariableArityParameter(self, ctx:MyJavaParser.VariableArityParameterContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableModifier.
    def enterVariableModifier(self, ctx:MyJavaParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableModifier.
    def exitVariableModifier(self, ctx:MyJavaParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#throwsT.
    def enterThrowsT(self, ctx:MyJavaParser.ThrowsTContext):
        pass

    # Exit a parse tree produced by MyJavaParser#throwsT.
    def exitThrowsT(self, ctx:MyJavaParser.ThrowsTContext):
        pass


    # Enter a parse tree produced by MyJavaParser#exceptionTypeList.
    def enterExceptionTypeList(self, ctx:MyJavaParser.ExceptionTypeListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#exceptionTypeList.
    def exitExceptionTypeList(self, ctx:MyJavaParser.ExceptionTypeListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#exceptionType.
    def enterExceptionType(self, ctx:MyJavaParser.ExceptionTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#exceptionType.
    def exitExceptionType(self, ctx:MyJavaParser.ExceptionTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#methodBody.
    def enterMethodBody(self, ctx:MyJavaParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by MyJavaParser#methodBody.
    def exitMethodBody(self, ctx:MyJavaParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by MyJavaParser#instanceInitializer.
    def enterInstanceInitializer(self, ctx:MyJavaParser.InstanceInitializerContext):
        pass

    # Exit a parse tree produced by MyJavaParser#instanceInitializer.
    def exitInstanceInitializer(self, ctx:MyJavaParser.InstanceInitializerContext):
        pass


    # Enter a parse tree produced by MyJavaParser#staticInitializer.
    def enterStaticInitializer(self, ctx:MyJavaParser.StaticInitializerContext):
        pass

    # Exit a parse tree produced by MyJavaParser#staticInitializer.
    def exitStaticInitializer(self, ctx:MyJavaParser.StaticInitializerContext):
        pass


    # Enter a parse tree produced by MyJavaParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:MyJavaParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:MyJavaParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#constructorModifier.
    def enterConstructorModifier(self, ctx:MyJavaParser.ConstructorModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#constructorModifier.
    def exitConstructorModifier(self, ctx:MyJavaParser.ConstructorModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#constructorDeclarator.
    def enterConstructorDeclarator(self, ctx:MyJavaParser.ConstructorDeclaratorContext):
        pass

    # Exit a parse tree produced by MyJavaParser#constructorDeclarator.
    def exitConstructorDeclarator(self, ctx:MyJavaParser.ConstructorDeclaratorContext):
        pass


    # Enter a parse tree produced by MyJavaParser#simpleTypeName.
    def enterSimpleTypeName(self, ctx:MyJavaParser.SimpleTypeNameContext):
        pass

    # Exit a parse tree produced by MyJavaParser#simpleTypeName.
    def exitSimpleTypeName(self, ctx:MyJavaParser.SimpleTypeNameContext):
        pass


    # Enter a parse tree produced by MyJavaParser#constructorBody.
    def enterConstructorBody(self, ctx:MyJavaParser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by MyJavaParser#constructorBody.
    def exitConstructorBody(self, ctx:MyJavaParser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by MyJavaParser#explicitConstructorInvocation.
    def enterExplicitConstructorInvocation(self, ctx:MyJavaParser.ExplicitConstructorInvocationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#explicitConstructorInvocation.
    def exitExplicitConstructorInvocation(self, ctx:MyJavaParser.ExplicitConstructorInvocationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:MyJavaParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:MyJavaParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#enumBody.
    def enterEnumBody(self, ctx:MyJavaParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by MyJavaParser#enumBody.
    def exitEnumBody(self, ctx:MyJavaParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by MyJavaParser#enumConstantList.
    def enterEnumConstantList(self, ctx:MyJavaParser.EnumConstantListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#enumConstantList.
    def exitEnumConstantList(self, ctx:MyJavaParser.EnumConstantListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#enumConstant.
    def enterEnumConstant(self, ctx:MyJavaParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by MyJavaParser#enumConstant.
    def exitEnumConstant(self, ctx:MyJavaParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by MyJavaParser#enumConstantModifier.
    def enterEnumConstantModifier(self, ctx:MyJavaParser.EnumConstantModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#enumConstantModifier.
    def exitEnumConstantModifier(self, ctx:MyJavaParser.EnumConstantModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:MyJavaParser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:MyJavaParser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#recordDeclaration.
    def enterRecordDeclaration(self, ctx:MyJavaParser.RecordDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#recordDeclaration.
    def exitRecordDeclaration(self, ctx:MyJavaParser.RecordDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#recordHeader.
    def enterRecordHeader(self, ctx:MyJavaParser.RecordHeaderContext):
        pass

    # Exit a parse tree produced by MyJavaParser#recordHeader.
    def exitRecordHeader(self, ctx:MyJavaParser.RecordHeaderContext):
        pass


    # Enter a parse tree produced by MyJavaParser#recordComponentList.
    def enterRecordComponentList(self, ctx:MyJavaParser.RecordComponentListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#recordComponentList.
    def exitRecordComponentList(self, ctx:MyJavaParser.RecordComponentListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#recordComponent.
    def enterRecordComponent(self, ctx:MyJavaParser.RecordComponentContext):
        pass

    # Exit a parse tree produced by MyJavaParser#recordComponent.
    def exitRecordComponent(self, ctx:MyJavaParser.RecordComponentContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableArityRecordComponent.
    def enterVariableArityRecordComponent(self, ctx:MyJavaParser.VariableArityRecordComponentContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableArityRecordComponent.
    def exitVariableArityRecordComponent(self, ctx:MyJavaParser.VariableArityRecordComponentContext):
        pass


    # Enter a parse tree produced by MyJavaParser#recordComponentModifier.
    def enterRecordComponentModifier(self, ctx:MyJavaParser.RecordComponentModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#recordComponentModifier.
    def exitRecordComponentModifier(self, ctx:MyJavaParser.RecordComponentModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#recordBody.
    def enterRecordBody(self, ctx:MyJavaParser.RecordBodyContext):
        pass

    # Exit a parse tree produced by MyJavaParser#recordBody.
    def exitRecordBody(self, ctx:MyJavaParser.RecordBodyContext):
        pass


    # Enter a parse tree produced by MyJavaParser#recordBodyDeclaration.
    def enterRecordBodyDeclaration(self, ctx:MyJavaParser.RecordBodyDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#recordBodyDeclaration.
    def exitRecordBodyDeclaration(self, ctx:MyJavaParser.RecordBodyDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#compactConstructorDeclaration.
    def enterCompactConstructorDeclaration(self, ctx:MyJavaParser.CompactConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#compactConstructorDeclaration.
    def exitCompactConstructorDeclaration(self, ctx:MyJavaParser.CompactConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:MyJavaParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:MyJavaParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#normalInterfaceDeclaration.
    def enterNormalInterfaceDeclaration(self, ctx:MyJavaParser.NormalInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#normalInterfaceDeclaration.
    def exitNormalInterfaceDeclaration(self, ctx:MyJavaParser.NormalInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceModifier.
    def enterInterfaceModifier(self, ctx:MyJavaParser.InterfaceModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceModifier.
    def exitInterfaceModifier(self, ctx:MyJavaParser.InterfaceModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceExtends.
    def enterInterfaceExtends(self, ctx:MyJavaParser.InterfaceExtendsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceExtends.
    def exitInterfaceExtends(self, ctx:MyJavaParser.InterfaceExtendsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfacePermits.
    def enterInterfacePermits(self, ctx:MyJavaParser.InterfacePermitsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfacePermits.
    def exitInterfacePermits(self, ctx:MyJavaParser.InterfacePermitsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceBody.
    def enterInterfaceBody(self, ctx:MyJavaParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceBody.
    def exitInterfaceBody(self, ctx:MyJavaParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:MyJavaParser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:MyJavaParser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:MyJavaParser.ConstantDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#constantDeclaration.
    def exitConstantDeclaration(self, ctx:MyJavaParser.ConstantDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#constantModifier.
    def enterConstantModifier(self, ctx:MyJavaParser.ConstantModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#constantModifier.
    def exitConstantModifier(self, ctx:MyJavaParser.ConstantModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:MyJavaParser.InterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceMethodDeclaration.
    def exitInterfaceMethodDeclaration(self, ctx:MyJavaParser.InterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#interfaceMethodModifier.
    def enterInterfaceMethodModifier(self, ctx:MyJavaParser.InterfaceMethodModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#interfaceMethodModifier.
    def exitInterfaceMethodModifier(self, ctx:MyJavaParser.InterfaceMethodModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#annotationInterfaceDeclaration.
    def enterAnnotationInterfaceDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#annotationInterfaceDeclaration.
    def exitAnnotationInterfaceDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#annotationInterfaceBody.
    def enterAnnotationInterfaceBody(self, ctx:MyJavaParser.AnnotationInterfaceBodyContext):
        pass

    # Exit a parse tree produced by MyJavaParser#annotationInterfaceBody.
    def exitAnnotationInterfaceBody(self, ctx:MyJavaParser.AnnotationInterfaceBodyContext):
        pass


    # Enter a parse tree produced by MyJavaParser#annotationInterfaceMemberDeclaration.
    def enterAnnotationInterfaceMemberDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#annotationInterfaceMemberDeclaration.
    def exitAnnotationInterfaceMemberDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#annotationInterfaceElementDeclaration.
    def enterAnnotationInterfaceElementDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceElementDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#annotationInterfaceElementDeclaration.
    def exitAnnotationInterfaceElementDeclaration(self, ctx:MyJavaParser.AnnotationInterfaceElementDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#annotationInterfaceElementModifier.
    def enterAnnotationInterfaceElementModifier(self, ctx:MyJavaParser.AnnotationInterfaceElementModifierContext):
        pass

    # Exit a parse tree produced by MyJavaParser#annotationInterfaceElementModifier.
    def exitAnnotationInterfaceElementModifier(self, ctx:MyJavaParser.AnnotationInterfaceElementModifierContext):
        pass


    # Enter a parse tree produced by MyJavaParser#defaultValue.
    def enterDefaultValue(self, ctx:MyJavaParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by MyJavaParser#defaultValue.
    def exitDefaultValue(self, ctx:MyJavaParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by MyJavaParser#annotation.
    def enterAnnotation(self, ctx:MyJavaParser.AnnotationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#annotation.
    def exitAnnotation(self, ctx:MyJavaParser.AnnotationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#normalAnnotation.
    def enterNormalAnnotation(self, ctx:MyJavaParser.NormalAnnotationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#normalAnnotation.
    def exitNormalAnnotation(self, ctx:MyJavaParser.NormalAnnotationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#elementValuePairList.
    def enterElementValuePairList(self, ctx:MyJavaParser.ElementValuePairListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#elementValuePairList.
    def exitElementValuePairList(self, ctx:MyJavaParser.ElementValuePairListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#elementValuePair.
    def enterElementValuePair(self, ctx:MyJavaParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by MyJavaParser#elementValuePair.
    def exitElementValuePair(self, ctx:MyJavaParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by MyJavaParser#elementValue.
    def enterElementValue(self, ctx:MyJavaParser.ElementValueContext):
        pass

    # Exit a parse tree produced by MyJavaParser#elementValue.
    def exitElementValue(self, ctx:MyJavaParser.ElementValueContext):
        pass


    # Enter a parse tree produced by MyJavaParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:MyJavaParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by MyJavaParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:MyJavaParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by MyJavaParser#elementValueList.
    def enterElementValueList(self, ctx:MyJavaParser.ElementValueListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#elementValueList.
    def exitElementValueList(self, ctx:MyJavaParser.ElementValueListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#markerAnnotation.
    def enterMarkerAnnotation(self, ctx:MyJavaParser.MarkerAnnotationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#markerAnnotation.
    def exitMarkerAnnotation(self, ctx:MyJavaParser.MarkerAnnotationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#singleElementAnnotation.
    def enterSingleElementAnnotation(self, ctx:MyJavaParser.SingleElementAnnotationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#singleElementAnnotation.
    def exitSingleElementAnnotation(self, ctx:MyJavaParser.SingleElementAnnotationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:MyJavaParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by MyJavaParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:MyJavaParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableInitializerList.
    def enterVariableInitializerList(self, ctx:MyJavaParser.VariableInitializerListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableInitializerList.
    def exitVariableInitializerList(self, ctx:MyJavaParser.VariableInitializerListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#block.
    def enterBlock(self, ctx:MyJavaParser.BlockContext):
        pass

    # Exit a parse tree produced by MyJavaParser#block.
    def exitBlock(self, ctx:MyJavaParser.BlockContext):
        pass


    # Enter a parse tree produced by MyJavaParser#blockStatements.
    def enterBlockStatements(self, ctx:MyJavaParser.BlockStatementsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#blockStatements.
    def exitBlockStatements(self, ctx:MyJavaParser.BlockStatementsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#blockStatement.
    def enterBlockStatement(self, ctx:MyJavaParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#blockStatement.
    def exitBlockStatement(self, ctx:MyJavaParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#localClassOrInterfaceDeclaration.
    def enterLocalClassOrInterfaceDeclaration(self, ctx:MyJavaParser.LocalClassOrInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#localClassOrInterfaceDeclaration.
    def exitLocalClassOrInterfaceDeclaration(self, ctx:MyJavaParser.LocalClassOrInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:MyJavaParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:MyJavaParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#localVariableType.
    def enterLocalVariableType(self, ctx:MyJavaParser.LocalVariableTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#localVariableType.
    def exitLocalVariableType(self, ctx:MyJavaParser.LocalVariableTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:MyJavaParser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:MyJavaParser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#statement.
    def enterStatement(self, ctx:MyJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#statement.
    def exitStatement(self, ctx:MyJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#statementNoShortIf.
    def enterStatementNoShortIf(self, ctx:MyJavaParser.StatementNoShortIfContext):
        pass

    # Exit a parse tree produced by MyJavaParser#statementNoShortIf.
    def exitStatementNoShortIf(self, ctx:MyJavaParser.StatementNoShortIfContext):
        pass


    # Enter a parse tree produced by MyJavaParser#statementWithoutTrailingSubstatement.
    def enterStatementWithoutTrailingSubstatement(self, ctx:MyJavaParser.StatementWithoutTrailingSubstatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#statementWithoutTrailingSubstatement.
    def exitStatementWithoutTrailingSubstatement(self, ctx:MyJavaParser.StatementWithoutTrailingSubstatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#emptyStatement_.
    def enterEmptyStatement_(self, ctx:MyJavaParser.EmptyStatement_Context):
        pass

    # Exit a parse tree produced by MyJavaParser#emptyStatement_.
    def exitEmptyStatement_(self, ctx:MyJavaParser.EmptyStatement_Context):
        pass


    # Enter a parse tree produced by MyJavaParser#labeledStatement.
    def enterLabeledStatement(self, ctx:MyJavaParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#labeledStatement.
    def exitLabeledStatement(self, ctx:MyJavaParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#labeledStatementNoShortIf.
    def enterLabeledStatementNoShortIf(self, ctx:MyJavaParser.LabeledStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by MyJavaParser#labeledStatementNoShortIf.
    def exitLabeledStatementNoShortIf(self, ctx:MyJavaParser.LabeledStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by MyJavaParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MyJavaParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MyJavaParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#statementExpression.
    def enterStatementExpression(self, ctx:MyJavaParser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#statementExpression.
    def exitStatementExpression(self, ctx:MyJavaParser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#ifThenStatement.
    def enterIfThenStatement(self, ctx:MyJavaParser.IfThenStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#ifThenStatement.
    def exitIfThenStatement(self, ctx:MyJavaParser.IfThenStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#ifThenElseStatement.
    def enterIfThenElseStatement(self, ctx:MyJavaParser.IfThenElseStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#ifThenElseStatement.
    def exitIfThenElseStatement(self, ctx:MyJavaParser.IfThenElseStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#ifThenElseStatementNoShortIf.
    def enterIfThenElseStatementNoShortIf(self, ctx:MyJavaParser.IfThenElseStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by MyJavaParser#ifThenElseStatementNoShortIf.
    def exitIfThenElseStatementNoShortIf(self, ctx:MyJavaParser.IfThenElseStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by MyJavaParser#assertStatement.
    def enterAssertStatement(self, ctx:MyJavaParser.AssertStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#assertStatement.
    def exitAssertStatement(self, ctx:MyJavaParser.AssertStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#switchStatement.
    def enterSwitchStatement(self, ctx:MyJavaParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#switchStatement.
    def exitSwitchStatement(self, ctx:MyJavaParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#switchBlock.
    def enterSwitchBlock(self, ctx:MyJavaParser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by MyJavaParser#switchBlock.
    def exitSwitchBlock(self, ctx:MyJavaParser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by MyJavaParser#switchRule.
    def enterSwitchRule(self, ctx:MyJavaParser.SwitchRuleContext):
        pass

    # Exit a parse tree produced by MyJavaParser#switchRule.
    def exitSwitchRule(self, ctx:MyJavaParser.SwitchRuleContext):
        pass


    # Enter a parse tree produced by MyJavaParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:MyJavaParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by MyJavaParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:MyJavaParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by MyJavaParser#switchLabel.
    def enterSwitchLabel(self, ctx:MyJavaParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by MyJavaParser#switchLabel.
    def exitSwitchLabel(self, ctx:MyJavaParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by MyJavaParser#caseConstant.
    def enterCaseConstant(self, ctx:MyJavaParser.CaseConstantContext):
        pass

    # Exit a parse tree produced by MyJavaParser#caseConstant.
    def exitCaseConstant(self, ctx:MyJavaParser.CaseConstantContext):
        pass


    # Enter a parse tree produced by MyJavaParser#whileStatement.
    def enterWhileStatement(self, ctx:MyJavaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#whileStatement.
    def exitWhileStatement(self, ctx:MyJavaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#whileStatementNoShortIf.
    def enterWhileStatementNoShortIf(self, ctx:MyJavaParser.WhileStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by MyJavaParser#whileStatementNoShortIf.
    def exitWhileStatementNoShortIf(self, ctx:MyJavaParser.WhileStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by MyJavaParser#doStatement.
    def enterDoStatement(self, ctx:MyJavaParser.DoStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#doStatement.
    def exitDoStatement(self, ctx:MyJavaParser.DoStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#forStatement.
    def enterForStatement(self, ctx:MyJavaParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#forStatement.
    def exitForStatement(self, ctx:MyJavaParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#forStatementNoShortIf.
    def enterForStatementNoShortIf(self, ctx:MyJavaParser.ForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by MyJavaParser#forStatementNoShortIf.
    def exitForStatementNoShortIf(self, ctx:MyJavaParser.ForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by MyJavaParser#basicForStatement.
    def enterBasicForStatement(self, ctx:MyJavaParser.BasicForStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#basicForStatement.
    def exitBasicForStatement(self, ctx:MyJavaParser.BasicForStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#basicForStatementNoShortIf.
    def enterBasicForStatementNoShortIf(self, ctx:MyJavaParser.BasicForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by MyJavaParser#basicForStatementNoShortIf.
    def exitBasicForStatementNoShortIf(self, ctx:MyJavaParser.BasicForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by MyJavaParser#forInit.
    def enterForInit(self, ctx:MyJavaParser.ForInitContext):
        pass

    # Exit a parse tree produced by MyJavaParser#forInit.
    def exitForInit(self, ctx:MyJavaParser.ForInitContext):
        pass


    # Enter a parse tree produced by MyJavaParser#forUpdate.
    def enterForUpdate(self, ctx:MyJavaParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by MyJavaParser#forUpdate.
    def exitForUpdate(self, ctx:MyJavaParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by MyJavaParser#statementExpressionList.
    def enterStatementExpressionList(self, ctx:MyJavaParser.StatementExpressionListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#statementExpressionList.
    def exitStatementExpressionList(self, ctx:MyJavaParser.StatementExpressionListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#enhancedForStatement.
    def enterEnhancedForStatement(self, ctx:MyJavaParser.EnhancedForStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#enhancedForStatement.
    def exitEnhancedForStatement(self, ctx:MyJavaParser.EnhancedForStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#enhancedForStatementNoShortIf.
    def enterEnhancedForStatementNoShortIf(self, ctx:MyJavaParser.EnhancedForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by MyJavaParser#enhancedForStatementNoShortIf.
    def exitEnhancedForStatementNoShortIf(self, ctx:MyJavaParser.EnhancedForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by MyJavaParser#breakStatement.
    def enterBreakStatement(self, ctx:MyJavaParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#breakStatement.
    def exitBreakStatement(self, ctx:MyJavaParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#continueStatement.
    def enterContinueStatement(self, ctx:MyJavaParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#continueStatement.
    def exitContinueStatement(self, ctx:MyJavaParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#returnStatement.
    def enterReturnStatement(self, ctx:MyJavaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#returnStatement.
    def exitReturnStatement(self, ctx:MyJavaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#throwStatement.
    def enterThrowStatement(self, ctx:MyJavaParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#throwStatement.
    def exitThrowStatement(self, ctx:MyJavaParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#synchronizedStatement.
    def enterSynchronizedStatement(self, ctx:MyJavaParser.SynchronizedStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#synchronizedStatement.
    def exitSynchronizedStatement(self, ctx:MyJavaParser.SynchronizedStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#tryStatement.
    def enterTryStatement(self, ctx:MyJavaParser.TryStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#tryStatement.
    def exitTryStatement(self, ctx:MyJavaParser.TryStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#catches.
    def enterCatches(self, ctx:MyJavaParser.CatchesContext):
        pass

    # Exit a parse tree produced by MyJavaParser#catches.
    def exitCatches(self, ctx:MyJavaParser.CatchesContext):
        pass


    # Enter a parse tree produced by MyJavaParser#catchClause.
    def enterCatchClause(self, ctx:MyJavaParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by MyJavaParser#catchClause.
    def exitCatchClause(self, ctx:MyJavaParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by MyJavaParser#catchFormalParameter.
    def enterCatchFormalParameter(self, ctx:MyJavaParser.CatchFormalParameterContext):
        pass

    # Exit a parse tree produced by MyJavaParser#catchFormalParameter.
    def exitCatchFormalParameter(self, ctx:MyJavaParser.CatchFormalParameterContext):
        pass


    # Enter a parse tree produced by MyJavaParser#catchType.
    def enterCatchType(self, ctx:MyJavaParser.CatchTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#catchType.
    def exitCatchType(self, ctx:MyJavaParser.CatchTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#finallyBlock.
    def enterFinallyBlock(self, ctx:MyJavaParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by MyJavaParser#finallyBlock.
    def exitFinallyBlock(self, ctx:MyJavaParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by MyJavaParser#tryWithResourcesStatement.
    def enterTryWithResourcesStatement(self, ctx:MyJavaParser.TryWithResourcesStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#tryWithResourcesStatement.
    def exitTryWithResourcesStatement(self, ctx:MyJavaParser.TryWithResourcesStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#resourceSpecification.
    def enterResourceSpecification(self, ctx:MyJavaParser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#resourceSpecification.
    def exitResourceSpecification(self, ctx:MyJavaParser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#resourceList.
    def enterResourceList(self, ctx:MyJavaParser.ResourceListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#resourceList.
    def exitResourceList(self, ctx:MyJavaParser.ResourceListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#resource.
    def enterResource(self, ctx:MyJavaParser.ResourceContext):
        pass

    # Exit a parse tree produced by MyJavaParser#resource.
    def exitResource(self, ctx:MyJavaParser.ResourceContext):
        pass


    # Enter a parse tree produced by MyJavaParser#variableAccess.
    def enterVariableAccess(self, ctx:MyJavaParser.VariableAccessContext):
        pass

    # Exit a parse tree produced by MyJavaParser#variableAccess.
    def exitVariableAccess(self, ctx:MyJavaParser.VariableAccessContext):
        pass


    # Enter a parse tree produced by MyJavaParser#yieldStatement.
    def enterYieldStatement(self, ctx:MyJavaParser.YieldStatementContext):
        pass

    # Exit a parse tree produced by MyJavaParser#yieldStatement.
    def exitYieldStatement(self, ctx:MyJavaParser.YieldStatementContext):
        pass


    # Enter a parse tree produced by MyJavaParser#pattern.
    def enterPattern(self, ctx:MyJavaParser.PatternContext):
        pass

    # Exit a parse tree produced by MyJavaParser#pattern.
    def exitPattern(self, ctx:MyJavaParser.PatternContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typePattern.
    def enterTypePattern(self, ctx:MyJavaParser.TypePatternContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typePattern.
    def exitTypePattern(self, ctx:MyJavaParser.TypePatternContext):
        pass


    # Enter a parse tree produced by MyJavaParser#expression.
    def enterExpression(self, ctx:MyJavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#expression.
    def exitExpression(self, ctx:MyJavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#primary.
    def enterPrimary(self, ctx:MyJavaParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MyJavaParser#primary.
    def exitPrimary(self, ctx:MyJavaParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MyJavaParser#primaryNoNewArray.
    def enterPrimaryNoNewArray(self, ctx:MyJavaParser.PrimaryNoNewArrayContext):
        pass

    # Exit a parse tree produced by MyJavaParser#primaryNoNewArray.
    def exitPrimaryNoNewArray(self, ctx:MyJavaParser.PrimaryNoNewArrayContext):
        pass


    # Enter a parse tree produced by MyJavaParser#pNNA.
    def enterPNNA(self, ctx:MyJavaParser.PNNAContext):
        pass

    # Exit a parse tree produced by MyJavaParser#pNNA.
    def exitPNNA(self, ctx:MyJavaParser.PNNAContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classLiteral.
    def enterClassLiteral(self, ctx:MyJavaParser.ClassLiteralContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classLiteral.
    def exitClassLiteral(self, ctx:MyJavaParser.ClassLiteralContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classInstanceCreationExpression.
    def enterClassInstanceCreationExpression(self, ctx:MyJavaParser.ClassInstanceCreationExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classInstanceCreationExpression.
    def exitClassInstanceCreationExpression(self, ctx:MyJavaParser.ClassInstanceCreationExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unqualifiedClassInstanceCreationExpression.
    def enterUnqualifiedClassInstanceCreationExpression(self, ctx:MyJavaParser.UnqualifiedClassInstanceCreationExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unqualifiedClassInstanceCreationExpression.
    def exitUnqualifiedClassInstanceCreationExpression(self, ctx:MyJavaParser.UnqualifiedClassInstanceCreationExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#classOrInterfaceTypeToInstantiate.
    def enterClassOrInterfaceTypeToInstantiate(self, ctx:MyJavaParser.ClassOrInterfaceTypeToInstantiateContext):
        pass

    # Exit a parse tree produced by MyJavaParser#classOrInterfaceTypeToInstantiate.
    def exitClassOrInterfaceTypeToInstantiate(self, ctx:MyJavaParser.ClassOrInterfaceTypeToInstantiateContext):
        pass


    # Enter a parse tree produced by MyJavaParser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:MyJavaParser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by MyJavaParser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:MyJavaParser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by MyJavaParser#arrayCreationExpression.
    def enterArrayCreationExpression(self, ctx:MyJavaParser.ArrayCreationExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#arrayCreationExpression.
    def exitArrayCreationExpression(self, ctx:MyJavaParser.ArrayCreationExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#arrayCreationExpressionWithoutInitializer.
    def enterArrayCreationExpressionWithoutInitializer(self, ctx:MyJavaParser.ArrayCreationExpressionWithoutInitializerContext):
        pass

    # Exit a parse tree produced by MyJavaParser#arrayCreationExpressionWithoutInitializer.
    def exitArrayCreationExpressionWithoutInitializer(self, ctx:MyJavaParser.ArrayCreationExpressionWithoutInitializerContext):
        pass


    # Enter a parse tree produced by MyJavaParser#arrayCreationExpressionWithInitializer.
    def enterArrayCreationExpressionWithInitializer(self, ctx:MyJavaParser.ArrayCreationExpressionWithInitializerContext):
        pass

    # Exit a parse tree produced by MyJavaParser#arrayCreationExpressionWithInitializer.
    def exitArrayCreationExpressionWithInitializer(self, ctx:MyJavaParser.ArrayCreationExpressionWithInitializerContext):
        pass


    # Enter a parse tree produced by MyJavaParser#dimExprs.
    def enterDimExprs(self, ctx:MyJavaParser.DimExprsContext):
        pass

    # Exit a parse tree produced by MyJavaParser#dimExprs.
    def exitDimExprs(self, ctx:MyJavaParser.DimExprsContext):
        pass


    # Enter a parse tree produced by MyJavaParser#dimExpr.
    def enterDimExpr(self, ctx:MyJavaParser.DimExprContext):
        pass

    # Exit a parse tree produced by MyJavaParser#dimExpr.
    def exitDimExpr(self, ctx:MyJavaParser.DimExprContext):
        pass


    # Enter a parse tree produced by MyJavaParser#arrayAccess.
    def enterArrayAccess(self, ctx:MyJavaParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by MyJavaParser#arrayAccess.
    def exitArrayAccess(self, ctx:MyJavaParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by MyJavaParser#fieldAccess.
    def enterFieldAccess(self, ctx:MyJavaParser.FieldAccessContext):
        pass

    # Exit a parse tree produced by MyJavaParser#fieldAccess.
    def exitFieldAccess(self, ctx:MyJavaParser.FieldAccessContext):
        pass


    # Enter a parse tree produced by MyJavaParser#methodInvocation.
    def enterMethodInvocation(self, ctx:MyJavaParser.MethodInvocationContext):
        pass

    # Exit a parse tree produced by MyJavaParser#methodInvocation.
    def exitMethodInvocation(self, ctx:MyJavaParser.MethodInvocationContext):
        pass


    # Enter a parse tree produced by MyJavaParser#argumentList.
    def enterArgumentList(self, ctx:MyJavaParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#argumentList.
    def exitArgumentList(self, ctx:MyJavaParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#methodReference.
    def enterMethodReference(self, ctx:MyJavaParser.MethodReferenceContext):
        pass

    # Exit a parse tree produced by MyJavaParser#methodReference.
    def exitMethodReference(self, ctx:MyJavaParser.MethodReferenceContext):
        pass


    # Enter a parse tree produced by MyJavaParser#postfixExpression.
    def enterPostfixExpression(self, ctx:MyJavaParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#postfixExpression.
    def exitPostfixExpression(self, ctx:MyJavaParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#pfE.
    def enterPfE(self, ctx:MyJavaParser.PfEContext):
        pass

    # Exit a parse tree produced by MyJavaParser#pfE.
    def exitPfE(self, ctx:MyJavaParser.PfEContext):
        pass


    # Enter a parse tree produced by MyJavaParser#postIncrementExpression.
    def enterPostIncrementExpression(self, ctx:MyJavaParser.PostIncrementExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#postIncrementExpression.
    def exitPostIncrementExpression(self, ctx:MyJavaParser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#postDecrementExpression.
    def enterPostDecrementExpression(self, ctx:MyJavaParser.PostDecrementExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#postDecrementExpression.
    def exitPostDecrementExpression(self, ctx:MyJavaParser.PostDecrementExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MyJavaParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MyJavaParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#preIncrementExpression.
    def enterPreIncrementExpression(self, ctx:MyJavaParser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#preIncrementExpression.
    def exitPreIncrementExpression(self, ctx:MyJavaParser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#preDecrementExpression.
    def enterPreDecrementExpression(self, ctx:MyJavaParser.PreDecrementExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#preDecrementExpression.
    def exitPreDecrementExpression(self, ctx:MyJavaParser.PreDecrementExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#unaryExpressionNotPlusMinus.
    def enterUnaryExpressionNotPlusMinus(self, ctx:MyJavaParser.UnaryExpressionNotPlusMinusContext):
        pass

    # Exit a parse tree produced by MyJavaParser#unaryExpressionNotPlusMinus.
    def exitUnaryExpressionNotPlusMinus(self, ctx:MyJavaParser.UnaryExpressionNotPlusMinusContext):
        pass


    # Enter a parse tree produced by MyJavaParser#castExpression.
    def enterCastExpression(self, ctx:MyJavaParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#castExpression.
    def exitCastExpression(self, ctx:MyJavaParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MyJavaParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MyJavaParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MyJavaParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MyJavaParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#shiftExpression.
    def enterShiftExpression(self, ctx:MyJavaParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#shiftExpression.
    def exitShiftExpression(self, ctx:MyJavaParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MyJavaParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MyJavaParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#equalityExpression.
    def enterEqualityExpression(self, ctx:MyJavaParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#equalityExpression.
    def exitEqualityExpression(self, ctx:MyJavaParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#andExpression.
    def enterAndExpression(self, ctx:MyJavaParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#andExpression.
    def exitAndExpression(self, ctx:MyJavaParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:MyJavaParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:MyJavaParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:MyJavaParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:MyJavaParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:MyJavaParser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:MyJavaParser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:MyJavaParser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx:MyJavaParser.ConditionalOrExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:MyJavaParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:MyJavaParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:MyJavaParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:MyJavaParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#assignment.
    def enterAssignment(self, ctx:MyJavaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyJavaParser#assignment.
    def exitAssignment(self, ctx:MyJavaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyJavaParser#leftHandSide.
    def enterLeftHandSide(self, ctx:MyJavaParser.LeftHandSideContext):
        pass

    # Exit a parse tree produced by MyJavaParser#leftHandSide.
    def exitLeftHandSide(self, ctx:MyJavaParser.LeftHandSideContext):
        pass


    # Enter a parse tree produced by MyJavaParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:MyJavaParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by MyJavaParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:MyJavaParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by MyJavaParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:MyJavaParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:MyJavaParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#lambdaParameters.
    def enterLambdaParameters(self, ctx:MyJavaParser.LambdaParametersContext):
        pass

    # Exit a parse tree produced by MyJavaParser#lambdaParameters.
    def exitLambdaParameters(self, ctx:MyJavaParser.LambdaParametersContext):
        pass


    # Enter a parse tree produced by MyJavaParser#lambdaParameterList.
    def enterLambdaParameterList(self, ctx:MyJavaParser.LambdaParameterListContext):
        pass

    # Exit a parse tree produced by MyJavaParser#lambdaParameterList.
    def exitLambdaParameterList(self, ctx:MyJavaParser.LambdaParameterListContext):
        pass


    # Enter a parse tree produced by MyJavaParser#lambdaParameter.
    def enterLambdaParameter(self, ctx:MyJavaParser.LambdaParameterContext):
        pass

    # Exit a parse tree produced by MyJavaParser#lambdaParameter.
    def exitLambdaParameter(self, ctx:MyJavaParser.LambdaParameterContext):
        pass


    # Enter a parse tree produced by MyJavaParser#lambdaParameterType.
    def enterLambdaParameterType(self, ctx:MyJavaParser.LambdaParameterTypeContext):
        pass

    # Exit a parse tree produced by MyJavaParser#lambdaParameterType.
    def exitLambdaParameterType(self, ctx:MyJavaParser.LambdaParameterTypeContext):
        pass


    # Enter a parse tree produced by MyJavaParser#lambdaBody.
    def enterLambdaBody(self, ctx:MyJavaParser.LambdaBodyContext):
        pass

    # Exit a parse tree produced by MyJavaParser#lambdaBody.
    def exitLambdaBody(self, ctx:MyJavaParser.LambdaBodyContext):
        pass


    # Enter a parse tree produced by MyJavaParser#switchExpression.
    def enterSwitchExpression(self, ctx:MyJavaParser.SwitchExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#switchExpression.
    def exitSwitchExpression(self, ctx:MyJavaParser.SwitchExpressionContext):
        pass


    # Enter a parse tree produced by MyJavaParser#constantExpression.
    def enterConstantExpression(self, ctx:MyJavaParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by MyJavaParser#constantExpression.
    def exitConstantExpression(self, ctx:MyJavaParser.ConstantExpressionContext):
        pass



del MyJavaParser