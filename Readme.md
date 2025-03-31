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

3. How to run the application 

A. Prerequisites
Before running the application, ensure you have the following installed:

Python (version 3.8 or higher)

PDM (Python Development Master, a package manager)

<<<<<<< HEAD
Installing PDM
If you haven't already installed PDM, you can do so by running:
=======
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
CMD ["python", "web_main.py"]
To build and run:
>>>>>>> 7b747dfbf14d7fa5afeb7a2c13ab58479bce2b5c

bash
Copy
Edit
pip install pdm
B. Setting Up the Project
Ensure that you have cloned or downloaded the project and that you've navigated to the project directory in your terminal. Once inside the project folder, run the following command to install the dependencies:

bash
Copy
Edit
pdm install
This will install all the necessary libraries and dependencies required for both the local and web applications.

C. Running the Local App (GUI)
The local app is a GUI application built using PyQt6. To run it, follow these steps:

Open a terminal and navigate to the project directory.

Run the following command:
pdm run gui_app.py(kindly make sure when u input data give spaces between the operators and operands to get the results)for eg:(* + 3 4 5)

This command will start the local app, and the GUI should appear. You can interact with it and use the features for local computation.

D. Running the Web App
The web app is a Flask-based application. To run it, follow these steps:

Open a terminal and navigate to the project directory.

Run the following command:
pdm run web_app.py(kindly make sure when u input data give spaces between the operators and operands to get the results)for eg:(* + 3 4 5)

This will start the Flask web server, and you can access the web app in your browser by visiting:
http://127.0.0.1:5000

E. Troubleshooting
If you encounter issues while running the application, check if all dependencies are installed correctly by running pdm install again.

Ensure that the Flask web server is not being blocked by a firewall or another program occupying port 5000.

F. Stopping the Applications
For the local app (GUI), simply close the window or press Ctrl + C in the terminal.

For the web app, you can stop the Flask server by pressing Ctrl + C in the terminal.


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

