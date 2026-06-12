from sympy import Matrix

from core.basic_matrix_operations import create_matrix, is_square_matrix

def check_square(macierz, function_name):
    """
    Sprawdza, czy macierz jest kwadratowa w kontekście zadanej funkcji.
    """

    if not is_square_matrix(macierz):
        return ValueError(f"Funkcja {function_name} wymaga macierzy kwadratowej.")
    
    return True

def is_invertible_matrix(macierz):
    """
    Sprawdza, czy macierz jest odwracalna.

    Warunki:
    - Macierz musi być kwadratowa.
    - Macierz jest odwracalna, jeśli jej wyznacznik jest różny od zera.
    """

    check_square(macierz, "sprawdzanie odwracalności")

    return macierz.det() != 0

def inverse_matrix(macierz):
    """
    Oblicza macierz odwrotną do zadanej, jeśli jest to możliwe.
    
    Warunki:
    - Macierz musi być kwadratowa.
    - Macierz musi być odwracalna (nie może mieć wyznacznika równego zero).
    """

    check_square(macierz, "odwracanie macierzy")
    
    if not is_invertible_matrix(macierz):
        return ValueError("Macierz nie jest odwracalna.")
    
    return macierz.inv()

def matrix_eigenvalues(macierz):
    """
    Oblicza wartości własne macierzy.
    Zwraca słownik, gdzie klucze to wartości własne, a wartości to ich algebraiczne krotności.

    Warunki:
    - Macierz musi być kwadratowa.
    """

    check_square(macierz, "obliczanie wartości własnych")
    
    return macierz.eigenvals()

def matrix_eigenvectors(macierz):
    """
    Oblicza wektory własne macierzy.
    Zwraca listę w formacie [(wartość własna, algebraiczna krotność, [wektory własne])].
    Wartość własna może mieć więcej niż jeden wektor własny, jeśli jest wielokrotna.

    Warunki:
    - Macierz musi być kwadratowa.
    """

    check_square(macierz, "obliczanie wektorów własnych")
    
    return macierz.eigenvects()

def is_diagonalizable(macierz):
    """
    Sprawdza, czy macierz jest diagonalizowalna.
    Macierz jest diagonalizowalna, jeśli liczba liniowo niezależnych wektorów własnych
    jest równa jej rozmiarowi (liczbie wierszy).

    Warunki:
    - Macierz musi być kwadratowa.
    """

    check_square(macierz, "sprawdzanie diagonalizowalności")
    
    eigenvectors = matrix_eigenvectors(macierz)
    eigensum = 0
    for eigenvalue, algebraic_multiplicity, vectors in eigenvectors:
        eigensum += len(vectors)
    return eigensum == macierz.rows

def diagonalize_matrix(macierz):
    """
    Diagonalizuje macierz, jeśli jest to możliwe.
    Zwraca macierz diagonalną D, macierz przejścia P i macierz odwrotną P^-1, takie że A = PDP^-1.
    Pokazuje informację, że A = P*D*P^(-1).

    Warunki:
    - Macierz musi być kwadratowa.
    - Macierz musi być diagonalizowalna.
    """

    check_square(macierz, "diagonalizacja macierzy")

    if not is_diagonalizable(macierz):
        return ValueError("Macierz nie jest diagonalizowalna.")
    
    P, D = macierz.diagonalize()
    P_inverse = P.inv()

    return {
        "D": D,
        "P": P,
        "P_inverse": P_inverse,
        "description": "A = P*D*P^(-1)"
    }

def has_complex_eigenvalues(macierz):
    """
    Sprawdza, czy macierz ma wartości własne zespolone, jeżeli jest kwadratowa.
    W przeciwnym razie zgłasza błąd.
    """

    check_square(macierz, "sprawdzanie wartości własnych zespolonych")

    eigenvalues = matrix_eigenvalues(macierz)

    for eigenvalue in eigenvalues.keys():
        real_part, imaginary_part = eigenvalue.as_real_imag()
        if imaginary_part != 0:
            return True

    return False