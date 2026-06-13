import sys
import unittest
from unittest.mock import MagicMock
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow

test_app = QApplication.instance()
if test_app is None:
    test_app = QApplication(sys.argv)

class Test_Button(unittest.TestCase):
    def test_clear(self):
        window = MainWindow()

        window.input_section = MagicMock()
        window.result_section = MagicMock()

        window.handle_clear()

        window.input_section.inputbox.clear.assert_called_once()
        window.result_section.result_display.clear.assert_called_once()
