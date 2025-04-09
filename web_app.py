from flask import Flask, request, render_template
from components.lexica import MyLexer
from components.parsers import MyParser, ASTParser

app = Flask(__name__)

lexer = MyLexer()
parser = MyParser()
ast_parser = ASTParser()

@app.route('/', methods=['GET'])
def calculator():
    # Renders the HTML template initially
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expr = request.form.get('expression', '').strip()
    result = None
    infix = None
    error = None

    if not expr:
        error = "Empty expression"
        return render_template('index.html', error=error)

    try:
        # Tokenize and parse the prefix expression
        tokens = list(lexer.tokenize(expr))
        result = parser.parse(lexer.tokenize(expr))
        ast = ast_parser.parse(lexer.tokenize(expr))
        infix = ast_parser.to_infix(ast)
    except Exception as e:
        error = str(e)

    return render_template('index.html', result=result, infix=infix, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
