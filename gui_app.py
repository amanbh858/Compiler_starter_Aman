import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                            QLineEdit, QPushButton, QHBoxLayout, QRadioButton,
                            QButtonGroup, QGridLayout)
from PyQt6.QtCore import Qt
from components.lexica import MyLexer
from components.parsers import MyParser, ASTParser

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prefix Calculator")
        self.setFixedSize(400, 500)
        
        self.lexer = MyLexer()
        self.parser = MyParser()
        self.ast_parser = ASTParser()
        
        self.current_input = ""
        self.init_ui()
    
    def init_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; height: 50px;")
        main_layout.addWidget(self.display)
        
        # Output options
        self.result_btn = QRadioButton("Show Result")
        self.infix_btn = QRadioButton("Show Infix")
        self.result_btn.setChecked(True)
        
        options_layout = QHBoxLayout()
        options_layout.addWidget(self.result_btn)
        options_layout.addWidget(self.infix_btn)
        main_layout.addLayout(options_layout)
        
        # Calculator buttons
        buttons_layout = QGridLayout()
        
        # Number buttons
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('0', 3, 0), ('(', 3, 1), (')', 3, 2),
            ('+', 0, 3), ('-', 1, 3), 
            ('*', 2, 3), ('/', 3, 3),
            ('C', 4, 0), ('⌫', 4, 1),
            ('Space', 4, 2), ('=', 4, 3)
        ]
        
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 10px;")
            button.clicked.connect(self.create_button_handler(text))
            buttons_layout.addWidget(button, row, col)
        
        main_layout.addLayout(buttons_layout)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    
    def create_button_handler(self, text):
        def handler():
            if text == '=':
                self.calculate()
            elif text == 'C':
                self.current_input = ""
                self.display.clear()
            elif text == '⌫':
                self.current_input = self.current_input[:-1]
                self.display.setText(self.current_input)
            elif text == 'Space':
                self.current_input += " "
                self.display.setText(self.current_input)
            else:
                self.current_input += text
                self.display.setText(self.current_input)
        return handler
    
    def calculate(self):
        if not self.current_input.strip():
            return
        
        try:
            if self.result_btn.isChecked():
                # Calculate result
                result = self.parser.parse(self.lexer.tokenize(self.current_input))
                self.display.setText(str(result))
                self.current_input = str(result)
            else:
                # Convert to infix
                ast = self.ast_parser.parse(self.lexer.tokenize(self.current_input))
                infix = self.ast_parser.to_infix(ast)
                self.display.setText(infix)
                self.current_input = infix
        except Exception as e:
            self.display.setText(f"Error: {str(e)}")
            self.current_input = ""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())