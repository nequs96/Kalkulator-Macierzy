from sympy import Matrix
from sympy import Basic
from core.basic_matrix_operations import (  create_matrix,
                                            is_dimension_match,
                                            is_square_matrix,
                                            matrix_addition,
                                            matrix_subtraction,
                                            matrix_by_matrix_multiplying,
                                            scalar_multiplying,
                                            transponent_matrix,
                                            matrix_exponentiation,
                                            matrix_rank,
                                            matrix_determinant,
                                            matrix_trace
                                        )

a = create_matrix([[4, 2], [1, 3]]) #poprawne wyniki dla wszystkich funkcji poniżej
b = create_matrix([[1, 2, 0], [0, 1, 0], [1, 1, 1], [2, 2, 2]]) #niepoprawne wyniki dla większości funkcji, ponieważ macierz b nie jest kwadratowa i ma inne wymiary niż macierz a
print("\n Przykładowe działanie kodu dla macierzy a i b:", a, b)

def test_is_dimension_match():
    print("\n--- Test funkcji is_dimension_match - czy macierze mają takie same wymiary ---")
    print("a - a:", is_dimension_match(a, a))
    print("a - b:", is_dimension_match(a, b))

def test_is_square_matrix():
    print("\n--- Test funkcji is_square_matrix - czy macierz jest kwadratowa ---")
    print("a jest kwadratowa:", is_square_matrix(a))
    print("b jest kwadratowa:", is_square_matrix(b))

def test_matrix_addition():
    print("\n--- Test funkcji matrix_addition - dodawanie macierzy ---")
    print("a + a =", matrix_addition(a, a))
    try:
        print("b + b =", matrix_addition(b, b))
    except Exception as e:
        print("Błąd dla b + b:", e)

def test_matrix_subtraction():
    print("\n--- Test funkcji matrix_subtraction - odejmowanie macierzy ---")
    print("a - a =", matrix_subtraction(a, a))
    try:
        print("b - b =", matrix_subtraction(b, b))
    except Exception as e:
        print("Błąd dla b - b:", e)

def test_matrix_by_matrix_multiplying():
    print("\n--- Test funkcji matrix_by_matrix_multiplying - mnożenie macierzy ---")
    print("a * a =", matrix_by_matrix_multiplying(a, a))
    try:
        print("b * b: ", matrix_by_matrix_multiplying(b, b))
    except Exception as e:
        print("Błąd dla b * b:", e)

def test_scalar_multiplying():
    print("\n--- Test funkcji scalar_multiplying - mnożenie macierzy przez liczbę ---")
    print("a * 2 =", scalar_multiplying(a, 2))
    print("b * 2 =", scalar_multiplying(b, 2))

def test_transponent_matrix():
    print("\n--- Test funkcji transponent_matrix - transponowanie macierzy ---")
    print("a^T =", transponent_matrix(a))
    print("b^T =", transponent_matrix(b))

def test_matrix_exponentiation():
    print("\n--- Test funkcji matrix_exponentiation - potęgowanie macierzy ---")
    print("a^2 =", matrix_exponentiation(a, 2))
    try:
        print("b^2: ", matrix_exponentiation(b, 2))
    except Exception as e:
        print("Błąd dla b^2:", e)

def test_matrix_rank():
    print("\n--- Test funkcji matrix_rank - rząd macierzy ---")
    print("rank(a) =", matrix_rank(a))
    print("rank(b) =", matrix_rank(b))

def test_determinant():
    print("\n--- Test funkcji matrix_determinant - wyznacznik macierzy ---")
    print("det(a) =", matrix_determinant(a))
    try:
        print("det(b):", matrix_determinant(b))
    except Exception as e:
        print("Błąd dla det(b):", e)

def test_trace():
    print("\n--- Test funkcji matrix_trace - ślad macierzy ---")
    print("trace(a) =", matrix_trace(a))
    try:
        print("trace(b)", matrix_trace(b))
    except Exception as e:
        print("Błąd dla trace(b):", e)

def start_test():
    test_is_dimension_match()
    test_is_square_matrix()
    test_matrix_addition()
    test_matrix_subtraction()
    test_matrix_by_matrix_multiplying()
    test_scalar_multiplying()
    test_transponent_matrix()
    test_matrix_exponentiation()
    test_matrix_rank()
    test_determinant()
    test_trace()
start_test()
