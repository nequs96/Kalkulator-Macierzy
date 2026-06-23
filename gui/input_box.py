from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class InputBox(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.examples = QLabel("""
det (wyznacznik)                           transpose (transpozycja)
add (dodawanie)                            diagonalize (diagonalizacja)   
trace (slad)                               eigenvalues (wartosci wlasne)
eigenvectors (wektory wlasne)              complex_eigenvalues (zespolone wart. wlasne)
subtract (odejmowanie)                     multiply(mnozenie)
scalar_multiply (mnozenie przez skalar)    power (potegowanie)
rank (rzad)                                inverse(odwracanie)""")    
        self.examples.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.examples)
        font = QFont("Cascadia Code", 10)
        font.setStyleHint(QFont.StyleHint.Monospace)
        self.examples.setFont(font)

        self.inputbox = QLineEdit()
        self.inputbox.setPlaceholderText("Wpisz komende np det([[1,2],[3,4]])")
        layout.addWidget(self.inputbox)

        buttons_layout = QHBoxLayout()
        self.button1 = QPushButton("oblicz")
        self.button2 = QPushButton("wyczysc")
        buttons_layout.addWidget(self.button1)
        buttons_layout.addWidget(self.button2)
        layout.addLayout(buttons_layout)