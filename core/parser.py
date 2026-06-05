from dataclasses import dataclass
import ast
import re

from sympy import Matrix


@dataclass
class ParsedCommand:
    operation: str
    arguments: list
    raw_text: str


class CommandParser:
    def __init__(self) -> None:
        self.operation_aliases = {
            "det": "det",
            "wyznacznik": "det",

            "rank": "rank",
            "rzad": "rank",
            "rząd": "rank",

            "transpose": "transpose",
            "transpozycja": "transpose",

            "multiply": "multiply",
            "mnozenie": "multiply",
            "mnożenie": "multiply",

            "inverse": "inverse",
            "odwrotna": "inverse",

            "eigenvalues": "eigenvalues",
            "wartosci_wlasne": "eigenvalues",
            "wartości_własne": "eigenvalues",

            "eigenvectors": "eigenvectors",
            "wektory_wlasne": "eigenvectors",
            "wektory_własne": "eigenvectors",

            "diagonalize": "diagonalize",
            "diagonalizacja": "diagonalize",
        }
