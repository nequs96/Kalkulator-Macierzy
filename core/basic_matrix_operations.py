"""Podstawowe operacje na macierzach."""

from typing import Any, Sequence

from sympy import Basic, Matrix


def create_matrix(data: Sequence[Sequence[Any]]) -> Matrix:
    """
    Zamienia podany obiekt (listę) na macierz używając biblioteki sympy.
    """
    return Matrix(data)


def is_dimension_match(macierz1: Matrix, macierz2: Matrix) -> bool:
    """
    Sprawdza, czy dwie macierze mają ten sam wymiar.
    """
    return macierz1.shape == macierz2.shape


def is_square_matrix(macierz: Matrix) -> bool:
    """
    Sprawdza, czy macierz jest kwadratowa.
    """
    return macierz.rows == macierz.cols


def matrix_addition(macierz1: Matrix, macierz2: Matrix) -> Matrix | ValueError:
    """
    Dodaje dwie macierze i zwraca wynik, jeżeli mają ten sam rozmiar.
    W przeciwnym razie zwraca błąd.
    """
    if not is_dimension_match(macierz1, macierz2):
        return ValueError(
            "Macierze muszą mieć ten sam rozmiar, aby można je było dodać."
        )

    return macierz1 + macierz2


def matrix_subtraction(macierz1: Matrix, macierz2: Matrix) -> Matrix | ValueError:
    """
    Odejmuje drugą macierz od pierwszej i zwraca wynik, jeżeli mają ten sam rozmiar.
    W przeciwnym razie zwraca błąd.
    """
    if not is_dimension_match(macierz1, macierz2):
        return ValueError(
            "Macierze muszą mieć ten sam rozmiar, aby można je było odjąć."
        )

    return macierz1 - macierz2


def matrix_by_matrix_multiplying(
    macierz1: Matrix,
    macierz2: Matrix,
) -> Matrix | ValueError:
    """
    Klasyczny iloczyn macierzy; mnoży dwie macierze i zwraca wynik,
    jeżeli mają odpowiednie wymiary.
    W przeciwnym razie zwraca błąd.
    """
    if not is_dimension_match(macierz1, macierz2):
        return ValueError(
            "Macierze muszą mieć ten sam rozmiar, aby można je było mnożyć."
        )

    return macierz1 * macierz2


def matrix_by_matrix_multiplying_Hadamarda(
    macierz1: Matrix,
    macierz2: Matrix,
) -> Matrix | ValueError:
    """
    Obsługuje mnożenie macierzy element po elemencie,
    jeżeli mają odpowiednie wymiary.
    W przeciwnym razie zwraca błąd.
    """
    if not is_dimension_match(macierz1, macierz2):
        return ValueError(
            "Macierze muszą mieć ten sam rozmiar, aby można je było mnożyć."
        )

    return macierz1 * macierz2


def scalar_multiplying(
    macierz: Matrix,
    skalar: object,
) -> Matrix | ValueError:

    """
    Mnoży macierz przez skalar i zwraca wynik.
    """
    if not isinstance(skalar, (int, float, Basic)):
        return ValueError("Skalar musi być liczbą całkowitą lub zmiennoprzecinkową.")

    return skalar * macierz


def transponent_matrix(macierz: Matrix) -> Matrix:
    """
    Zwraca transpozycję macierzy.
    """
    return macierz.T


def matrix_exponentiation(macierz: Matrix, potega: object) -> Matrix | ValueError:
    """
    Podnosi macierz do potęgi w sensie algebraicznym, tzn.
    wykonuje wielokrotne mnożenie macierzy przez samą siebie.
    Aby to było możliwe, macierz musi być kwadratowa, potega musi być liczbą całkowitą.
    Jezeli potega jest ujemna, macierz musi być odwracalna.
    """
    if not is_square_matrix(macierz):
        return ValueError(
            "Macierz musi być kwadratowa, aby można ją było podnieść do potęgi 'macierzowej'."
        )

    if not isinstance(potega, int):
        return ValueError("Potęga musi być liczbą całkowitą typu int.")

    if potega < 0 and macierz.det() == 0:
        return ValueError("Jeśli potęga jest ujemna, to macierz musi być niesingularna.")

    return macierz ** potega


def elementwise_matrix_exponentiation(
    macierz: Matrix,
    potega: Basic | int | float,
) -> Matrix | ValueError:
    """
    Podnosi macierz do potęgi (element po elemencie) i zwraca wynik,
    jeżeli macierz jest kwadratowa.
    W przeciwnym razie zwraca błąd.
    """
    if not is_square_matrix(macierz):
        return ValueError("Macierz musi być kwadratowa.")

    return macierz.applyfunc(lambda element: element ** potega)


def matrix_rank(macierz: Matrix) -> int:
    """
    Zwraca rząd macierzy.
    """
    return macierz.rank()


def matrix_determinant(macierz: Matrix) -> Basic | ValueError:
    """
    Zwraca wyznacznik macierzy, jeżeli jest kwadratowa.
    W przeciwnym razie zwraca błąd.
    """
    if not is_square_matrix(macierz):
        return ValueError(
            "Macierz musi być kwadratowa, aby można było obliczyć jej wyznacznik."
        )

    return macierz.det()


def matrix_trace(macierz: Matrix) -> Basic | ValueError:
    """
    Zwraca ślad macierzy, jeżeli jest kwadratowa.
    W przeciwnym razie zwraca błąd.
    """
    if not is_square_matrix(macierz):
        return ValueError(
            "Macierz musi być kwadratowa, aby można było obliczyć jej ślad."
        )

    return macierz.trace()