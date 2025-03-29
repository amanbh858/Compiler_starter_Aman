from sly import Parser
from sly.yacc import YaccProduction
from components.lexica import MyLexer

class MyParser(Parser):
    tokens = MyLexer.tokens
    
    def __init__(self):
        self.names = {}
    
    @_('PLUS expr expr',
       'TIMES expr expr')
    def expr(self, p):
        if p[0] == '+':
            return p[1] + p[2]
        elif p[0] == '*':
            return p[1] * p[2]
    
    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER
    
    def error(self, p):
        if p:
            print(f"Syntax error at token {p.type}")
        else:
            print("Syntax error at EOF")

class ASTParser(Parser):
    tokens = MyLexer.tokens
    
    def __init__(self):
        self.names = {}
    
    @_('PLUS expr expr')
    def expr(self, p):
        return ('+', p.expr0, p.expr1)
    
    @_('TIMES expr expr')
    def expr(self, p):
        return ('*', p.expr0, p.expr1)
    
    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER
    
    def error(self, p):
        if p:
            print(f"Syntax error at token {p.type}")
        else:
            print("Syntax error at EOF")
    
    def to_infix(self, ast):
        if isinstance(ast, tuple):
            op, left, right = ast
            left_expr = self.to_infix(left)
            right_expr = self.to_infix(right)
            # Handle precedence - only need parentheses if lower precedence inside higher
            if op == '+' and isinstance(left, tuple) and left[0] == '*':
                left_expr = f'({left_expr})'
            if op == '+' and isinstance(right, tuple) and right[0] == '*':
                right_expr = f'({right_expr})'
            return f"{left_expr} {op} {right_expr}"
        return str(ast)