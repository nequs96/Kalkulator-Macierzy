from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PySide6.QtCore import Qt

class ResultView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.result_title = QLabel("Wynik: ")
        self.result_title.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.result_title)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True) 
        layout.addWidget(self.result_display)