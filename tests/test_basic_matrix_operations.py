from sympy import Matrix
from sympy import Basic
import unittest
from core.basic_matrix_operations import (  create_matrix,
                                            is_dimension_match,
                                            is_square_matrix,
                                            matrix_addition,
                                            matrix_subtraction,
                                            matrix_by_matrix_multiplying,
                                            matrix_by_matrix_multiplying_Hadamarda,
                                            scalar_multiplying,
                                            matrix_exponentiation,
                                            matrix_determinant,
                                            matrix_trace
                                        )
class TestBasicMatrixOperations(unittest.TestCase):
    a = create_matrix([[4, 2], [1, 3]]) #poprawne wyniki dla wszystkich funkcji poniżej
    b = create_matrix([[1, 2, 0], [0, 1, 0], [1, 1, 1], [2, 2, 2]]) #niepoprawne wyniki dla większości funkcji, ponieważ macierz b nie jest kwadratowa i ma inne wymiary niż macierz a
    """Testy kodu dla macierzy a i b:"""

    def test_is_dimension_match(self):
        """Test funkcji is_dimension_match - czy macierze mają takie same wymiary"""
        assert is_dimension_match(self.a, self.a) == True
        assert is_dimension_match(self.a, self.b) == False

    def test_is_square_matrix(self):
        """Test funkcji is_square_matrix - czy macierz jest kwadratowa"""
        assert is_square_matrix(self.a) == True
        assert is_square_matrix(self.b) == False

    def test_matrix_addition(self):
        """Test funkcji matrix_addition - dodawanie macierzy"""
        assert matrix_addition(self.a, self.a) == create_matrix([[8, 4], [2, 6]])
        assert isinstance(matrix_addition(self.a, self.b), ValueError)
        assert str(matrix_addition(self.a, self.b)) == "Macierze muszą mieć ten sam rozmiar, aby można je było dodać."

    def test_matrix_subtraction(self):
        """Test funkcji matrix_subtraction - odejmowanie macierzy"""
        assert matrix_subtraction(self.a, self.a) == create_matrix([[0, 0], [0, 0]])
        assert isinstance(matrix_subtraction(self.a, self.b), ValueError)
        assert str(matrix_subtraction(self.a, self.b)) == "Macierze muszą mieć ten sam rozmiar, aby można je było odjąć."

    def test_matrix_by_matrix_multiplying(self):
        """Test funkcji matrix_by_matrix_multiplying - mnożenie macierzy"""
        assert matrix_by_matrix_multiplying(self.a, self.a) == create_matrix([[18, 14], [7, 11]])
        assert isinstance(matrix_by_matrix_multiplying(self.a, self.b), ValueError)
        assert str(matrix_by_matrix_multiplying(self.a, self.b)) == "Macierze muszą mieć ten sam rozmiar, aby można je było mnożyć."

    def test_matrix_by_matrix_multiplying_Hadamarda(self):
            """Test funkcji matrix_by_matrix_multiplying_Hadamarda - mnożenie macierzy element po elemencie"""
            assert matrix_by_matrix_multiplying_Hadamarda(self.a, self.a) == create_matrix([[18, 14], [7, 11]])
            assert isinstance(matrix_by_matrix_multiplying_Hadamarda(self.a, self.b), ValueError)
            assert str(matrix_by_matrix_multiplying_Hadamarda(self.a, self.b)) == "Macierze muszą mieć ten sam rozmiar, aby można je było mnożyć."

    def test_scalar_multiplying(self):
        """Test funkcji scalar_multiplying - mnożenie macierzy przez liczbę"""
        assert scalar_multiplying(self.a, 2) == create_matrix([[8, 4], [2, 6]])
        zt = scalar_multiplying(self.a, "abc")  # zły typ
        assert isinstance(zt, ValueError)
        assert str(zt) == "Skalar musi być liczbą całkowitą lub zmiennoprzecinkową."

    def test_matrix_exponentiation(self):
        """Test funkcji matrix_exponentiation - potęgowanie macierzy (macierz @ macierz ...)"""
        assert matrix_exponentiation(self.a, 2) == create_matrix([[18, 14], [7, 11]])
        assert isinstance(matrix_exponentiation(self.b, 2), ValueError)
        assert str(matrix_exponentiation(self.b, 2)) == "Macierz musi być kwadratowa, aby można ją było podnieść do potęgi 'macierzowej'."
        assert isinstance(matrix_exponentiation(self.a, 2.5), ValueError)
        assert str(matrix_exponentiation(self.a, 2.5)) == "Potęga musi być liczbą całkowitą typu int."  
        assert isinstance(matrix_exponentiation(create_matrix([[1, 2], [2, 4]]), -1), ValueError)
        assert str(matrix_exponentiation(create_matrix([[1, 2], [2, 4]]), -1)) == "Jeśli potęga jest ujemna, to macierz musi być niesingularna."



    def test_determinant(self):
        """Test funkcji matrix_determinant - wyznacznik macierzy"""
        assert matrix_determinant(self.a) == 10
        assert isinstance(matrix_determinant(self.b), ValueError)
        assert str(matrix_determinant(self.b)) == "Macierz musi być kwadratowa, aby można było obliczyć jej wyznacznik."

    def test_trace(self):
        """Test funkcji matrix_trace - ślad macierzy"""
        assert matrix_trace(self.a) == 7
        assert isinstance(matrix_trace(self.b), ValueError)
        assert str(matrix_trace(self.b)) == "Macierz musi być kwadratowa, aby można było obliczyć jej ślad."

