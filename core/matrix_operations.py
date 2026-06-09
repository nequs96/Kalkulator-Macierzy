from sympy import Matrix
from sympy import Basic

def create_matrix(data):
    """
    Zamienia podany obiekt (listę) na macierz używając biblioteki sympy.
    """
    return Matrix(data)

def is_dimension_match(macierz1, macierz2):
    """
    Sprawdza, czy dwie macierze mają ten sam wymiar.
    """
    return macierz1.shape == macierz2.shape

def is_square_matrix(macierz):
    """
    Sprawdza, czy macierz jest kwadratowa.
    """
    return macierz.rows == macierz.cols

def matrix_addition(macierz1, macierz2):
    """
    Dodaje dwie macierze i zwraca wynik, jeżeli mają ten sam rozmiar.
    W przeciwnym razie zgłasza błąd.
    """

    if not is_dimension_match(macierz1, macierz2):
        raise ValueError("Macierze muszą mieć ten sam rozmiar, aby można je było dodać.")

    return macierz1 + macierz2

def matrix_subtraction(macierz1, macierz2):
    """
    Odejmuje drugą macierz od pierwszej i zwraca wynik, jeżeli mają ten sam rozmiar.
    W przeciwnym razie zgłasza błąd.
    """

    if not is_dimension_match(macierz1, macierz2):
        raise ValueError("Macierze muszą mieć ten sam rozmiar, aby można je było odjąć.")

    return macierz1 - macierz2

def matrix_by_matrix_multiplying(macierz1, macierz2):
    """
    Mnoży dwie macierze i zwraca wynik, jeżeli mają odpowiednie wymiary.
    W przeciwnym razie zgłasza błąd.
    """

    if not is_dimension_match(macierz1, macierz2):
        raise ValueError("Macierze muszą mieć ten sam rozmiar, aby można je było mnożyć.")

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

    if not is_square_matrix(macierz):
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

    if not is_square_matrix(macierz):
        raise ValueError("Macierz musi być kwadratowa, aby można było obliczyć jej wyznacznik.")

    return macierz.det()

def matrix_trace(macierz):
    """
    Zwraca ślad macierzy, jeżeli jest kwadratowa.
    W przeciwnym razie zgłasza błąd.
    """

    if not is_square_matrix(macierz):
        raise ValueError("Macierz musi być kwadratowa, aby można było obliczyć jej ślad.")

    return macierz.trace()


def format_for_gui(result):
    """
    Formatuje wynik macierzowych operacji do formatu odpowiedniego dla GUI.
    """
    try:
        if isinstance(result, Basic):
            return str(result)
    except ImportError:
        pass

    if isinstance(result, Matrix): #zamienia macierz na listę list
        return result.tolist()

    elif isinstance(result, dict): #przerabia słowniki 
        return {str(key): format_for_gui(value) for key, value in result.items()}

    elif isinstance(result, list): #tworzy liste i "formatuje jej elementy"
        return [format_for_gui(item) for item in result]

    elif isinstance(result, tuple): #krotki traktuje jak listy
        return [format_for_gui(item) for item in result]

    elif isinstance(result, set): #zbiory traktuje jak listy, ale dodatkowo sortuje, żeby były w ustalonej kolejności
        return [format_for_gui(item) for item in sorted(result, key=str)]
    
    return str(result) #wszystko inne zamieniamy na string