"""Główne okno aplikacji kalkulatora macierzy."""

from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from core.command_dispatcher import execute_command
from core.matrix_formatter import format_result
from gui.input_box import InputBox
from gui.result_view import ResultView


class MainWindow(QMainWindow):
    """Główne okno aplikacji zawierające wejście użytkownika i wyniki."""

    def __init__(self) -> None:
        """Inicjalizuje główne okno aplikacji i łączy sygnały przycisków."""
        super().__init__()

        self.setWindowTitle("Kalkulator Macierzy")
        self.resize(600, 500)

        widget = QWidget()
        layout = QVBoxLayout(widget)

        label1 = QLabel("Kalkulator Macierzy")
        label1.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(label1)

        self.input_section = InputBox()
        self.result_section = ResultView()

        layout.addWidget(self.input_section)
        layout.addWidget(self.result_section)

        self.setCentralWidget(widget)

        self.input_section.button1.clicked.connect(self.handle_calculate)
        self.input_section.button2.clicked.connect(self.handle_clear)

    def handle_calculate(self) -> None:
        """Pobiera komendę użytkownika, wykonuje ją i wyświetla wynik."""
        command = self.input_section.inputbox.text()

        try:
            raw = execute_command(command)
            formatted = format_result(raw)

            history_entry = f">>> {command}\n{formatted}\n{'-' * 30}"

        except Exception as error:
            history_entry = f">>> {command}\n[!] BŁĄD: {str(error)}\n{'-' * 30}"

        self.result_section.result_display.append(history_entry)
        self.input_section.inputbox.clear()

    def handle_clear(self) -> None:
        """Czyści pole wejściowe oraz historię wyników."""
        self.input_section.inputbox.clear()
        self.result_section.result_display.clear()