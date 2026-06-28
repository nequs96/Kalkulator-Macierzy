"""Widżet wyświetlający wyniki obliczeń."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PySide6.QtCore import Qt


class ResultView(QWidget):
    """Widżet odpowiedzialny za prezentację wyników użytkownikowi."""

    def __init__(self) -> None:
        """Inicjalizuje widok odpowiedzialny za wyświetlanie wyników."""
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.result_title = QLabel("Wynik: ")
        self.result_title.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )
        layout.addWidget(self.result_title)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)