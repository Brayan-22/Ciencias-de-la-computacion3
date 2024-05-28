from antlr4 import *
from services.myantlr4.MyJavaVisitor import MyJavaVisitor as MyJavaVisitor
from services.myantlr4.MyJavaParser import MyJavaParser as MyJavaParser
class MyVistorNinfija(MyJavaVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.temp = 0
        self.tableSimb = {}
    # Visit a parse tree produced by MyJavaParser#compilationUnit.
    def visitCompilationUnit(self, ctx:MyJavaParser.CompilationUnitContext):
        return self.visitChildren(ctx)
    
    def visitLiteral(self, ctx: MyJavaParser.LiteralContext):
        return ctx.getText()
    
    def visitSuma(self, ctx: MyJavaParser.SumaContext):
        expr1Value = self.visit(ctx.expression(0))
        expr2Value = self.visit(ctx.expression(1))
        # self.pila[self.temp] = 
        print(f"t{self.temp} = {expr1Value} + {expr2Value} ")
        r = str(f"t{self.temp}")
        self.temp = self.temp+1
        return float(expr1Value) + float(expr2Value)
    
    def visitResta(self, ctx: MyJavaParser.RestaContext):
        expr1Value =  self.visit(ctx.expression(0))
        expr2Value = self.visit(ctx.expression(1))
        print(f"t{self.temp} = {expr1Value} - {expr2Value} ")
        r = str(f"t{self.temp}")
        self.temp = self.temp+1
        return float(expr1Value) - float(expr2Value)
    
    def visitMult(self, ctx: MyJavaParser.MultContext):
        expr1Value =  self.visit(ctx.expression(0))
        expr2Value = self.visit(ctx.expression(1))
        print(f"t{self.temp} = {expr1Value} * {expr2Value} ")
        r = str(f"t{self.temp}")
        self.temp = self.temp+1
        return float(expr1Value) * float(expr2Value)
    
    def visitDiv(self, ctx: MyJavaParser.DivContext):
        expr1Value =  self.visit(ctx.expression(0))
        expr2Value = self.visit(ctx.expression(1))
        print(f"t{self.temp} = {expr1Value} / {expr2Value} ")
        r = str(f"t{self.temp}")
        self.temp = self.temp+1
        return float(expr1Value) / float(expr2Value)
    
    def visitVariableDeclarator(self, ctx: MyJavaParser.VariableDeclaratorContext):
        self.temp = 1
        var = ctx.Identifier().getText()
        value = self.visit(ctx.variableInitializer())
        self.tableSimb[var] = value
        print(f"{var} = {value}")    
        
            
    def visitVariableInitializer(self, ctx: MyJavaParser.VariableInitializerContext):
        return self.visit(ctx.expression())
    
