Report 
Compiler Project Report: Prefix Notation Calculator
Author: Aman Bhardwaj
Email: amanbh858@gmail.com

1. Project Overview
A calculator that evaluates arithmetic expressions in prefix notation with two operators (+, *), where * has higher precedence than +.

Features
Input: Prefix notation (e.g., + * 3 4 5)

Output Options:

Computed result (e.g., 17)

Infix notation with parentheses (e.g., 3 * 4 + 5)

Operator Precedence: * evaluated before + (e.g., + * 2 3 4 → 2 * 3 + 4 = 10).

Grammar (BNF)
bnf
Copy
<Expression> ::= <Operator> <Expression> <Expression> | <Number>
<Operator>   ::= '+' | '*'
<Number>     ::= Integer
Parser Type
Top-down recursive descent parser (SLY library).

Two variants:

Immediate evaluation (MyParser): Computes results during parsing.

AST-based (ASTParser): Generates Abstract Syntax Tree for infix conversion.

Key Components
File	Purpose
lexica.py	Tokenizes input into numbers (NUMBER) and operators (+, *).
parsers.py	Implements grammar rules and handles precedence.
main.py	PyQt6 GUI with input/output fields and mode selection (Result/Infix).

3. Deployment Methods

A. PDM-Based Setup
bash
Copy
# Initialize project
pdm init

# Install dependencies
pdm add sly==0.5 PyQt6==6.8.1

# Run application
pdm run python main.py

B. Docker Implementation
dockerfile
Copy
# Dockerfile
FROM python:3.9-slim
WORKDIR /app

# Install system dependencies for PyQt6
RUN apt-get update && apt-get install -y libxcb-xinerama0

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application
COPY . .

# Launch GUI (X11 forwarding required)
CMD ["python", "main.py"]
To build and run:

bash
Copy
docker build -t prefix-calculator .
docker run -e DISPLAY=host.docker.internal:0 prefix-calculator

4.Example Inputs(I also shared some screenshots)

Prefix Input	Result	Infix Output
+ * 3 4 5	     17	     3 * 4 + 5
* + 2 3 4	     20	     (2 + 3) * 4

4. Conclusion

The project demonstrates:

Lexical analysis and parsing of prefix notation.

Operator precedence handling during AST conversion.

Integration of compiler components with a GUI.

Dual deployment via PDM (development) and Docker (production)

