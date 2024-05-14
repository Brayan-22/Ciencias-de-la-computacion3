import sys
from antlr4 import *
from myantlr4.JavaParser import JavaParser as JavaParser
from myantlr4.JavaVisitor import JavaVisitor as JavaVisitor

class VisitorInterp(JavaVisitor):
    def __init__(self) -> None:
        self.fields = {
        }
        self.localVar={
        }
        self.analisiSintactico = []
        
        
        
    def visitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        self.analisiSintactico.append("Analisis sintactico\n\n")
        return self.visitChildren(ctx)
    
    def visitImportDeclaration(self, ctx: JavaParser.ImportDeclarationContext):
        importDec = f"importacion de libreria, sintaxis correcta \n{ctx.IMPORT().getText()} {ctx.qualifiedName().getText()} {ctx.DOT()} {ctx.MUL()} {ctx.SEMI()} \n"
        self.analisiSintactico.append(importDec)
        return self.visitChildren(ctx)
    
    def visitPackageDeclaration(self, ctx: JavaParser.PackageDeclarationContext):
        packageDec = f"Declaracion de paquete, sintaxis correcta \n{ctx.PACKAGE()} {ctx.qualifiedName().getText()} {ctx.SEMI()} \n"
        self.analisiSintactico.append(packageDec)
        return self.visitChildren(ctx)
    
    def visitClassOrInterfaceDeclaration(self, ctx: JavaParser.ClassOrInterfaceDeclarationContext):
        mods = "".join(self.visitClassOrInterfaceModifiers(ctx.classOrInterfaceModifiers()))
        classOrInterfaceDec = f"Declaracion de clase o interface, sintaxis correcta:\n{mods} {self.visitChildren(ctx)}"
        self.analisiSintactico.append(classOrInterfaceDec)
        return None
    
    # Visit a parse tree produced by JavaParser#classOrInterfaceModifiers.
    def visitClassOrInterfaceModifiers(self, ctx:JavaParser.ClassOrInterfaceModifiersContext):
        modifiers = []
        if ctx.classOrInterfaceModifier():
            for modifier in ctx.classOrInterfaceModifier():
                modifiers.append(self.visitClassOrInterfaceModifier(modifier))
        return modifiers
    
        # Visit a parse tree produced by JavaParser#classOrInterfaceModifier.
    def visitClassOrInterfaceModifier(self, ctx:JavaParser.ClassOrInterfaceModifierContext):
        return ctx.getText()+" "
    
    def visitClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        if ctx.normalClassDeclaration():
            return self.visitNormalClassDeclaration(ctx.normalClassDeclaration())
        elif ctx.enumDeclaration():
            return self.visitEnumDeclaration(ctx.enumDeclaration())
        return None
    
    # Visit a parse tree produced by JavaParser#normalClassDeclaration.
    def visitNormalClassDeclaration(self, ctx:JavaParser.NormalClassDeclarationContext):
        classDec = f"{ctx.CLASS().getText()} {ctx.IDENTIFIER()} {self.visitClassBody(ctx.classBody())}"
        return classDec
    
    # Visit a parse tree produced by JavaParser#classBody.
    def visitClassBody(self, ctx:JavaParser.ClassBodyContext):
        self.visitChildren(ctx)
        return f"{ctx.LBRACE().getText()} ... {ctx.RBRACE().getText()}"
    
    def visitClassBodyDeclaration(self, ctx: JavaParser.ClassBodyDeclarationContext):
        if ctx.modifiers():
            modificadores = self.visitModifiers(ctx.modifiers())
            print(modificadores)
        que = self.visitMemberDecl(ctx.memberDecl())
        if que is not None:
            #que[0] = array of (identificador = expression)
            #que[1] = type
            for q in que[0]:
                stx = f"Declaracion y asignacion, sintaxis correcta\n {' '.join(modificadores)} {que[1]} {q[0]} {q[1]} {q[2]} ;\n"
                self.analisiSintactico.append(stx)
                self.fields[q[0]] ={
                    "modificadores": modificadores,
                    "type":que[1],
                    "value":q[2]
                }
            return None
        else:
            print("metodo")
            print(modificadores)
            return None
        

    # Visit a parse tree produced by JavaParser#type.
    def visitType(self, ctx:JavaParser.TypeContext):
        if ctx.classOrInterfaceType():
            return self.visitClassOrInterfaceType(ctx)
        else:
            return ctx.primitiveType().getText()
    
        # Visit a parse tree produced by JavaParser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx:JavaParser.ClassOrInterfaceTypeContext):
        print(ctx.IDENTIFIER())
        return ctx.IDENTIFIER()
        
    def visitMemberDeclaration(self, ctx: JavaParser.MemberDeclarationContext):
        member_type = self.visitType(ctx.type_())
        if ctx.methodDeclaration():
            pass
        elif ctx.fieldDeclaration():
            campos =  self.visitFieldDeclaration(ctx.fieldDeclaration())
            return campos,member_type
        else:
            pass
        
    def visitFieldDeclaration(self, ctx: JavaParser.FieldDeclarationContext):
        return self.visitVariableDeclarators(ctx.variableDeclarators())
    
    
    # Visit a parse tree produced by JavaParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:JavaParser.VariableDeclaratorsContext):
        campos = []
        if ctx.variableDeclarator():
            for varDec in ctx.variableDeclarator():
                tupla = self.visitVariableDeclarator(varDec)
                campos.append(tupla)
        return campos


    # Visit a parse tree produced by JavaParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        name = ctx.variableDeclaratorId().getText()
        if ctx.variableInitializer():
            assignmentOperator = ctx.ASSIGN().getText()
            value = self.visitVariableInitializer(ctx.variableInitializer())
        else:
            assignmentOperator = None
            value = None
        return name,assignmentOperator,value
    
    # Visit a parse tree produced by JavaParser#variableInitializer.
    def visitVariableInitializer(self, ctx:JavaParser.VariableInitializerContext):
        return ctx.getText()
    
    
    def visitMemberDecl(self, ctx: JavaParser.MemberDeclContext):
        if ctx.memberDeclaration():
            return self.visitMemberDeclaration(ctx.memberDeclaration())
        else:
            
            return self.visitMainMethod(ctx.mainMethod())

    # Visit a parse tree produced by JavaParser#mainMethod.
    def visitMainMethod(self, ctx:JavaParser.MainMethodContext):
        
    
    
    def visitType(self, ctx: JavaParser.TypeContext):
        if ctx.primitiveType():
            return self.visitPrimitiveType(ctx.primitiveType())
        elif ctx.classOrInterfaceType():
            return self.visitClassOrInterfaceType(ctx.classOrInterfaceType()) 
        else: 
            return self.visitChildren(ctx)
    
    # Visit a parse tree produced by JavaParser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx:JavaParser.ClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#primitiveType.
    def visitPrimitiveType(self, ctx:JavaParser.PrimitiveTypeContext):
        self.visitChildren(ctx)
        return ctx.getText()    
    
    
    # Visit a parse tree produced by JavaParser#modifiers.
    def visitModifiers(self, ctx:JavaParser.ModifiersContext):
        modifiers = []
        if ctx.modifier():
            for modifier in ctx.modifier():
                modifiers.append(self.visitModifier(modifier))
        self.visitChildren(ctx)
        return modifiers

    def visitModifier(self, ctx: JavaParser.ModifierContext):
        self.visitChildren(ctx)
        return ctx.getText()
        

        
