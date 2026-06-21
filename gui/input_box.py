from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt

class InputBox(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.examples = QLabel("""
            det (wyznacznik) 
            add (dodawanie) 
            trace (slad)""")
        self.examples.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.examples)

        self.inputbox = QLineEdit()
        self.inputbox.setPlaceholderText("Wpisz komende np det([[1,2],[3,4]])")
        layout.addWidget(self.inputbox)

        buttons_layout = QHBoxLayout()
        self.button1 = QPushButton("oblicz")
        self.button2 = QPushButton("wyczysc")
        buttons_layout.addWidget(self.button1)
        buttons_layout.addWidget(self.button2)
        layout.addLayout(buttons_layout)