from sympy import Matrix


def create_matrix(data):
    """
    Zamienia podany obiekt (listę) na macierz używając biblioteki sympy.
    """
    return Matrix(data)


def matrix_addition(macierz1, macierz2):
    """
    Dodaje dwie macierze i zwraca wynik, jeżeli mają ten sam rozmiar.
    W przeciwnym razie zgłasza błąd.
    """

    if macierz1.shape != macierz2.shape:
        raise ValueError("Macierze muszą mieć ten sam rozmiar, aby można je było dodać.")

    return macierz1 + macierz2

def matrix_subtraction(macierz1, macierz2):
    """
    Odejmuje drugą macierz od pierwszej i zwraca wynik, jeżeli mają ten sam rozmiar.
    W przeciwnym razie zgłasza błąd.
    """

    if macierz1.shape != macierz2.shape:
        raise ValueError("Macierze muszą mieć ten sam rozmiar, aby można je było odjąć.")

    return macierz1 - macierz2

def matrix_by_matrix_multiplying(macierz1, macierz2):
    """
    Mnoży dwie macierze i zwraca wynik, jeżeli mają odpowiednie wymiary.
    W przeciwnym razie zgłasza błąd.
    """

    if macierz1.cols != macierz2.rows:
        raise ValueError(
            "Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy, "
            "aby można je było mnożyć."
        ) 

    return macierz1 * macierz2

def scalar_multiplying(macierz, skalar):
    """
    Mnoży macierz przez skalar i zwraca wynik.
    """

    if not isinstance(skalar, (int, float)):
        raise ValueError("Skalar musi być liczbą całkowitą lub zmiennoprzecinkową.")

    return macierz * skalar

def transponent_matrix(macierz):
    """
    Zwraca transpozycję macierzy.
    """

    return macierz.T

def matrix_exponentiation(macierz, potega):
    """
    Podnosi macierz do potęgi i zwraca wynik, jeżeli macierz jest kwadratowa.
    W przeciwnym razie zgłasza błąd.
    """

    if macierz.rows != macierz.cols:
        raise ValueError("Macierz musi być kwadratowa, aby można ją było podnieść do potęgi.")

    if not isinstance(potega, int) or potega < 0:
        raise ValueError("Potęga musi być nieujemną liczbą całkowitą.")

    return macierz ** potega

def matrix_rank(macierz):
    """
    Zwraca rząd macierzy.
    """

    return macierz.rank()

def matrix_determinant(macierz):
    """
    Zwraca wyznacznik macierzy, jeżeli jest kwadratowa.
    W przeciwnym razie zgłasza błąd.
    """

    if macierz.rows != macierz.cols:
        raise ValueError("Macierz musi być kwadratowa, aby można było obliczyć jej wyznacznik.")

    return macierz.det()

def matrix_trace(macierz):
    """
    Zwraca ślad macierzy, jeżeli jest kwadratowa.
    W przeciwnym razie zgłasza błąd.
    """

    if macierz.rows != macierz.cols:
        raise ValueError("Macierz musi być kwadratowa, aby można było obliczyć jej ślad.")

    return macierz.trace()

def is_square_matrix(macierz):
    """
    Sprawdza, czy macierz jest kwadratowa.
    """

    return macierz.rows == macierz.cols

def is_invertible_matrix(macierz):
    """
    Sprawdza, czy macierz jest odwracalna.
    """

    if not is_square_matrix(macierz):
        raise ValueError("Macierz musi być kwadratowa, aby można było sprawdzić jej odwracalność.")
    
    if matrix_determinant(macierz) == 0:
        return False
    
    return True

def is_diagonalizable_matrix(macierz):
    """
    Sprawdza, czy macierz jest diagonalizowalna (korzystająć z funkcji is_diagonalizable() z biblioteki sympy).
    """

    if not is_square_matrix(macierz):
        raise ValueError("Macierz musi być kwadratowa, aby można było sprawdzić jej diagonalizowalność.")
    
    return macierz.is_diagonalizable()




# 3. macierz_odwrotna(macierz)

# 4. wartosci_wlasne(macierz)

# 5. wektory_wlasne(macierz)

# 6. diagonalizacja_macierzy(macierz)


# 10. sprawdz_czy_odwracalna(macierz)


# 12. zamiana_macierzy_na_tekst(macierz)

# 13. zapisz_macierz_do_pliku(macierz, nazwa_pliku)

# 14. wczytaj_macierz_z_pliku(nazwa_pliku)

if __name__ == "__main__":
    macierz1_data = [[1, 2], [3, 4]]
    macierz2_data = [[5, 6], [7, 8]]

    macierz1 = matrix(macierz1_data)
    macierz2 = matrix(macierz2_data)

    print("Macierz 1:")
    print(macierz1)

    print("Macierz 2:")
    print(macierz2)

    print("Dodawanie:")
    print(matrix_addition(macierz1, macierz2))

    print("Mnożenie:")
    print(matrix_by_matrix_multiplying(macierz1, macierz2))