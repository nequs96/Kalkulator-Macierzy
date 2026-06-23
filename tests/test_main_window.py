import sys
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow

test_app = QApplication.instance()
if test_app is None:
    test_app = QApplication(sys.argv)

class Test_Button(unittest.TestCase):
    def test_clear(self):
        window = MainWindow()

        with patch.object(window, 'handle_clear') as mock_handle_clear:

            window.input_section.button2.clicked.emit()

            mock_handle_clear.assert_called_once()

    def test_button1(self):
        window = MainWindow()
        
        window.input_section.inputbox.setText("")
        window.result_section.result_display.setText = MagicMock()

        window.input_section.button1.clicked.emit()

        window.result_section.result_display.setText.assert_not_called()
