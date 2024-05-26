from services.myantlr4.MyJavaListener import MyJavaListener
from services.myantlr4.MyJavaParser import MyJavaParser

class MyListener(MyJavaListener):
    def __init__(self) -> None:
        super().__init__()
        
    def enterCompilationUnit(self, ctx: MyJavaParser.CompilationUnitContext):
        print("Entra en la unidad de compilacion")
        return super().enterCompilationUnit(ctx)
    def exitCompilationUnit(self, ctx: MyJavaParser.CompilationUnitContext):
        return super().exitCompilationUnit(ctx)
    def enterClassDeclaration(self, ctx: MyJavaParser.ClassDeclarationContext):
        print("Entra en el cuerpo de una clase")
        return super().enterClassDeclaration(ctx)