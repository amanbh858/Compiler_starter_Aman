import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QHBoxLayout, QRadioButton, QButtonGroup
from components.lexica import MyLexer
from components.parsers import MyParser, ASTParser

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prefix Calculator")
        self.setGeometry(100, 100, 600, 400)
        
        self.lexer = MyLexer()
        self.parser = MyParser()
        self.ast_parser = ASTParser()
        
        self.init_ui()
    
    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter prefix expression (e.g., '+ * 3 4 5')")
        
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        
        # Output options
        self.result_btn = QRadioButton("Result")
        self.infix_btn = QRadioButton("Infix Notation")
        self.result_btn.setChecked(True)
        
        output_options = QHBoxLayout()
        output_options.addWidget(self.result_btn)
        output_options.addWidget(self.infix_btn)
        
        # Calculate button
        self.calculate_btn = QPushButton("Calculate")
        self.calculate_btn.clicked.connect(self.calculate)
        
        layout.addWidget(self.input_text)
        layout.addLayout(output_options)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.output_text)
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def calculate(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            return
        
        try:
            if self.result_btn.isChecked():
                # Calculate result
                result = self.parser.parse(self.lexer.tokenize(text))
                self.output_text.setPlainText(str(result))
            else:
                # Convert to infix
                ast = self.ast_parser.parse(self.lexer.tokenize(text))
                infix = self.ast_parser.to_infix(ast)
                self.output_text.setPlainText(infix)
        except Exception as e:
            self.output_text.setPlainText(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())