from sly import Lexer

class MyLexer(Lexer):
    tokens = {NUMBER, PLUS, TIMES}
    ignore = ' \t'  

    # Match operators (unchanged)
    PLUS = r'\+'
    TIMES = r'\*'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Handle errors (skip illegal characters)
    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1

    def tokenize(self, text):
        spaced_text = []
        for char in text:
            if char in '+-*/':  # Add more operators if needed
                spaced_text.append(f' {char} ')
            elif char.isdigit():
                spaced_text.append(char)
            else:
                spaced_text.append(char)
        spaced_text = ''.join(spaced_text)
        
        # Now tokenize the spaced string
        return super().tokenize(spaced_text)

if __name__ == '__main__':
    # Test cases
    tests = [
        '+*345',    # Should work like "+ * 3 4 5"
        '*+123',     # Should work like "* + 1 2 3"
        '+ 2 3',     # Original spaced input 
        '+++123',    # Edge case: multiple operators
    ]
    
    lexer = MyLexer()
    for data in tests:
        print(f"\nInput: '{data}'")
        for tok in lexer.tokenize(data):
            print(tok)