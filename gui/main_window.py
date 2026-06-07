from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit,
    QPushButton, QTextEdit )
from PySide6.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator Macierzy")
        self.resize(600, 500)

        widget = QWidget()

        label1 = QLabel("Kalkulator Macierzy")
        label1.setAlignment(Qt.AlignTop | Qt.AlignHCenter)


        layout = QVBoxLayout()
        layout.addWidget(label1)
        widget.setLayout(layout)

        examples = QLabel("""
                          det (wyznacznik) 
                          add (dodawanie) 
                          tr (slad)""")
        layout.addWidget(examples)
        examples.setAlignment(Qt.AlignLeft)

        button1 = QPushButton("oblicz")
        layout.addWidget(button1)

        button2 = QPushButton("wyczysc")
        layout.addWidget(button2)

        self.inputbox = QLineEdit()
        self.inputbox.setPlaceholderText("Wpisz komende np det[(1,2),(3,4)]")
        layout.addWidget(self.inputbox)

        result = QLabel("Wynik: ")
        result.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(result)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
        


        self.setCentralWidget(widget)

app = QApplication()

window = MainWindow()
window.show()

app.exec()


