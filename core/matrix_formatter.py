from core.basic_matrix_operations import *
from core.basic_matrix_operations import *
from sympy import Matrix, Basic

def format_result(result):
    """
    Funkcja format_result zamienia różne typy wyników (macierze, liczby,
    słowniki, listy, krotki, błędy) na czytelny tekst, który można wyświetlić w GUI.
    """

    if isinstance(result, Exception):
        return f"Błąd: {str(result)}"

    if isinstance(result, Basic): #sympy basic na tekst
        return str(result)

    if isinstance(result, Matrix): #formatowanie macierzy jako teskt
        rows = []
        for row in result.tolist():
            row_text = "  ".join(str(el) for el in row)
            rows.append(f"[ {row_text} ]")
        return "\n".join(rows)

    if isinstance(result, dict): #słownik na tekst
        lines = []
        for key, value in result.items():
            lines.append(f"{key}: {format_result(value)}")
        return "\n".join(lines)

    if isinstance(result, list): #formatowanie listy na tekst
        return "[" + ", ".join(format_result(el) for el in result) + "]"

    if isinstance(result, tuple): #poprawione formatowanie krotki na tekst
        return "(" + ", ".join(format_result(el) for el in result) + ")"

    return str(result) #Liczby i wszystko inne — zamieniamy na tekst
