from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator Macierzy")
        self.resize(600, 500)

        widget = QWidget()

        label1 = QLabel("Kalkulator Macierzy")
        label1.setAlignment(Qt.AlignTop)
        label1.setAlignment(Qt.AlignHCenter)
        layout = QVBoxLayout()
        layout.addWidget(label1)
       
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication()

window = MainWindow()
window.show()

app.exec()


