from flask import Flask, request, jsonify
from components.lexica import MyLexer
from components.parsers import MyParser, ASTParser

app = Flask(__name__)

# Your existing Python lexer and parser will be used here
lexer = MyLexer()
parser = MyParser()
ast_parser = ASTParser()

@app.route('/')
def calculator():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Prefix Calculator</title>
        <style>
            body { font-family: Arial; max-width: 500px; margin: 0 auto; padding: 20px; }
            input, button { padding: 10px; margin: 5px 0; width: 100%; }
            #result { margin-top: 20px; padding: 15px; background: #f5f5f5; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Prefix Calculator</h1>
        <form method="POST" action="/calculate">
            <input type="text" name="expression" 
                   placeholder="+ * 3 4 5" required>
            <button type="submit">Calculate</button>
        </form>
        <div id="result">
            {% if result %}
                <p><b>Result:</b> {{ result }}</p>
                <p><b>Infix:</b> {{ infix }}</p>
            {% endif %}
            {% if error %}
                <p class="error">{{ error }}</p>
            {% endif %}
        </div>
    </body>
    </html>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    expr = request.form.get('expression', '').strip()
    
    if not expr:
        return '''
        <p class="error">Error: Empty expression</p>
        <a href="/">Try again</a>
        '''
    
    try:
        # Tokenize using your Python lexer
        tokens = list(lexer.tokenize(expr))
        
        # Calculate result using your Python parser
        result = parser.parse(lexer.tokenize(expr))
        
        # Generate infix using your Python AST parser
        ast = ast_parser.parse(lexer.tokenize(expr))
        infix = ast_parser.to_infix(ast)
        
        return f'''
        <p><b>Result:</b> {result}</p>
        <p><b>Infix:</b> {infix}</p>
        <a href="/">New calculation</a>
        '''
        
    except Exception as e:
        return f'''
        <p class="error">Error: {str(e)}</p>
        <a href="/">Try again</a>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)