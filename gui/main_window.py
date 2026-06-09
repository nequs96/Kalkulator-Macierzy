from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit,
    QPushButton, QTextEdit )
from PySide6.QtCore import Qt

from gui.input_box import InputBox
from gui.result_view import ResultView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator Macierzy")
        self.resize(600, 500)

        widget = QWidget()
        layout = QVBoxLayout(widget)

        label1 = QLabel("Kalkulator Macierzy")
        label1.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(label1)

        self.input_section = InputBox()
        self.result_section = ResultView()

        layout.addWidget(self.input_section)
        layout.addWidget(self.result_section)

        self.setCentralWidget(widget)

        self.input_section.button1.clicked.connect(self.handle_calculate)
        self.input_section.button2.clicked.connect(self.handle_clear)

    def handle_calculate(self):
        command = self.input_section.inputbox.text()
        
        if not command.strip():
            return
        
        #to do zastapienia
        raw = execute_command(command)
        formatted = format_result(raw)
        
        self.result_section.result_display.setText(formatted)

    def handle_clear(self):
        self.input_section.inputbox.clear()
        self.result_section.result_display.clear()

