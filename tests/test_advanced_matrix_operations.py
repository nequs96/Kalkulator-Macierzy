import unittest
from sympy import I as j, Rational, Matrix

from core.advanced_matrix_operations import (
                                            create_matrix, 
                                             inverse_matrix, 
                                             matrix_eigenvalues, 
                                             matrix_eigenvectors, 
                                             diagonalize_matrix, 
                                             has_complex_eigenvalues
                                            )

class TestInverse_EigenOperations(unittest.TestCase):
    """
    Testy kodu dla funkcji związanych z macierzami odwracalnymi, wartościami własnymi, 
    wektorami własnymi i diagonalizacją.
    """

    #macierz odwracalna
    invertible_matrix = create_matrix([[4, 2], [1, 3]])
    #macierz nieodwracalna
    non_invertible_matrix = create_matrix([[1, 2], [2, 4]])
    #prosta macierz diagonalna
    diagonal_matrix = create_matrix([[5, 0], [0, 3]])


    def test_inverse_matrix_invertible(self):
            assert inverse_matrix(self.invertible_matrix) == create_matrix([[Rational(3, 10), Rational(-1, 5)], 
                                                               [Rational(-1, 10), Rational(2, 5)]])

    def test_inverse_matrix_non_invertible(self):
        result = inverse_matrix(self.non_invertible_matrix)

        assert isinstance(result, ValueError)
        assert str(result) == "Macierz nie jest odwracalna."

    def test_eigenvalues_of_diagonal_matrix(self):
        assert matrix_eigenvalues(self.diagonal_matrix) == {5: 1, 3: 1}

    def test_eigenvectors_of_diagonal_matrix(self):
        results = matrix_eigenvectors(self.diagonal_matrix)
        assert len(results) == 2
        assert results[0][0] == 3
        assert results[0][1] == 1
        assert results[1][0] == 5
        assert results[1][1] == 1
        assert results[0][2] == [create_matrix([[0], [1]])]
        assert results[1][2] == [create_matrix([[1], [0]])]


class TestDiagonalization(unittest.TestCase):
    """
    Testy kodu dla funkcji związanych z diagonalizacją macierzy i sprawdzaniem, 
    czy macierz ma zespolone wartości własne.
    """

    non_invertible_matrix = create_matrix([[1, 2], [2, 4]])
    diagonal_matrix = create_matrix([[5, 0], [0, 3]])
    complex_diagonal_matrix = create_matrix([[j, 0], [0, 1-j]])
    diagonalizable_matrix = create_matrix([[2, 1], [0, 3]])
    non_diagonalizable_matrix = create_matrix([[1, 1], [0, 1]])


    def test_diagonalize_diagonalizable_matrix(self):
        results = diagonalize_matrix(self.diagonalizable_matrix)
        assert results["D"] == create_matrix([[2, 0], [0, 3]])
        assert results["P"] == create_matrix([[1, 1], [0,1]])
        assert results["P_inverse"] == create_matrix([[1, -1], [0, 1]])
        assert results["P"] * results["D"] * results["P_inverse"] == self.diagonalizable_matrix

    def test_diagonalize_nondiagonalizable_matrix(self):
        result = diagonalize_matrix(self.non_diagonalizable_matrix)

        assert isinstance(result, ValueError)
        assert str(result) == "Macierz nie jest diagonalizowalna."

    def test_has_complex_eigenvalues(self):
        assert has_complex_eigenvalues(self.complex_diagonal_matrix) == True

    def test_has_no_complex_eigenvalues(self):
        assert has_complex_eigenvalues(self.diagonal_matrix) == False

