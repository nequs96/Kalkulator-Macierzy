from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit
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

        self.inputbox = QLineEdit()
        self.inputbox.setPlaceholderText("Wpisz komende np det[(1,2),(3,4)]")
        layout.addWidget(self.inputbox)
        


        self.setCentralWidget(widget)

app = QApplication()

window = MainWindow()
window.show()

app.exec()


