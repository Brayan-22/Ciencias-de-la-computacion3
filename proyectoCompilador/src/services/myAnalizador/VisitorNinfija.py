from antlr4 import *
from services.myantlr4.MyJavaVisitor import MyJavaVisitor as MyJavaVisitor
from services.myantlr4.MyJavaParser import MyJavaParser as MyJavaParser
class MyVistorNinfija(MyJavaVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.temp = 1
        self.pila = []
    # Visit a parse tree produced by MyJavaParser#compilationUnit.
    def visitCompilationUnit(self, ctx:MyJavaParser.CompilationUnitContext):
        return self.visitChildren(ctx)
    
    def visitLiteral(self, ctx: MyJavaParser.LiteralContext):
        return ctx.getText()
    
    def visitSuma(self, ctx: MyJavaParser.SumaContext):
        expr1Value = self.visit(ctx.expression(0))
        expr2Value = self.visit(ctx.expression(1))
        self.pila.append(f"t{self.temp} = {expr1Value} + {expr2Value} \n")
        r = str(f"t{self.temp}")
        self.temp = self.temp+1
        return r
    
    def visitResta(self, ctx: MyJavaParser.RestaContext):
        expr1Value =  self.visit(ctx.expression(0))
        expr2Value = self.visit(ctx.expression(1))
        self.pila.append(f"t{self.temp} = {expr1Value} - {expr2Value} \n")
        r = str(f"t{self.temp}")
        self.temp = self.temp+1
        return r    
    
    def visitMult(self, ctx: MyJavaParser.MultContext):
        expr1Value =  self.visit(ctx.expression(0))
        expr2Value = self.visit(ctx.expression(1))
        self.pila.append(f"t{self.temp} = {expr1Value} * {expr2Value} \n")
        r = str(f"t{self.temp}")
        self.temp = self.temp+1
        return r
    
    def visitDiv(self, ctx: MyJavaParser.DivContext):
        expr1Value =  self.visit(ctx.expression(0))
        expr2Value = self.visit(ctx.expression(1))
        self.pila.append(f"t{self.temp} = {expr1Value} / {expr2Value} \n")
        r = str(f"t{self.temp}")
        self.temp = self.temp+1
        return r
    
    def visitVariableDeclarator(self, ctx: MyJavaParser.VariableDeclaratorContext):
        var = ctx.Identifier().getText()
        value = self.visit(ctx.variableInitializer())
        self.pila.append(f"{var} = {value} \n")
            
    def visitVariableInitializer(self, ctx: MyJavaParser.VariableInitializerContext):
        return self.visit(ctx.expression())