from sly import Lexer

class MyLexer(Lexer):
    tokens = {NUMBER, PLUS, TIMES}
    ignore = ' \t'
    
    PLUS = r'\+'
    TIMES = r'\*'
    
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
    
    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1

if __name__ == '__main__':
    data = '+ * 3 4 5'
    lexer = MyLexer()
    for tok in lexer.tokenize(data):
        print(tok)