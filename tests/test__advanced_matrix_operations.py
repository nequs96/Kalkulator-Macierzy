from sympy import I as j 
from core.advanced_matrix_operations import (
                                            create_matrix, 
                                             inverse_matrix, 
                                             matrix_eigenvalues, 
                                             matrix_eigenvectors, 
                                             diagonalize_matrix, 
                                             has_complex_eigenvalues
                                            )

#macierz odwracalna
invertible_matrix = create_matrix([[4, 2], [1, 3]])

#macierz nieodwracalna
non_invertible_matrix = create_matrix([[1, 2], [2, 4]])

#prosta macierz diagonalna
diagonal_matrix = create_matrix([[5, 0], [0, 3]])

#prosta macierz diagonalna z zespolonymi wartościami własnymi
complex_diagonal_matrix = create_matrix([[j, 0], [0, 1-j]])

#macierz diagonalizowalna
diagonalizable_matrix = create_matrix([[2, 1], [0, 3]])

#macierz niediagonalizowalna
nondiagonalizable_matrix = create_matrix([[1, 1], [0, 1]])


print("Testowanei macierzy odwracalnej:")
print("Macierz:\n", invertible_matrix)
print("Odwrotność:\n", inverse_matrix(invertible_matrix))


print("\nTestowanie macierzy nieodwracalnej:")
print("Macierz:\n", non_invertible_matrix)
try:
    print("Próba odwrócenia macierzy:\n", inverse_matrix(non_invertible_matrix))
except ValueError as e:
    print("Błąd:", e)


print("\nTestowanie macierzy diagonalnej:")
print("Macierz:\n", diagonal_matrix)
print("Wartości własne:\n", matrix_eigenvalues(diagonal_matrix))
print("Wektory własne:\n", matrix_eigenvectors(diagonal_matrix))


print("\nTestowanie macierzy diagonalizowalnej:")
print("Macierz:\n", diagonalizable_matrix)
print("Wartości własne:\n", matrix_eigenvalues(diagonalizable_matrix))
print("Wektory własne:\n", matrix_eigenvectors(diagonalizable_matrix))

results = diagonalize_matrix(diagonalizable_matrix)

print("D:\n ", results["D"])
print("P:\n ", results["P"])
print("P^-1:\n ", results["P_inverse"])
print("Opis:\n ", results["description"])
print("Sprawdzanie, czy P * D * P^-1 równa się macierzy oryginalnej: ", 
      results["P"] * results["D"] * results["P_inverse"] == diagonalizable_matrix)


print("\nTestowanie macierzy niediagonalizowalnej:")
print("Macierz:\n", nondiagonalizable_matrix)
try:
    print("Próba zdiagonalizowania:\n", diagonalize_matrix(nondiagonalizable_matrix))
except ValueError as e:
    print("Błąd:", e)
print("Wartości własne:\n", matrix_eigenvalues(nondiagonalizable_matrix))
print("Wektory własne:\n", matrix_eigenvectors(nondiagonalizable_matrix))


print("\nTestowanie macierzy z zespolonymi wartościami własnymi:")
print("Macierz:\n", complex_diagonal_matrix)   
print("\nSprawdzanie, czy macierz ma zespolone wartości własne: ", has_complex_eigenvalues(complex_diagonal_matrix))
print("Wartości własne:\n", matrix_eigenvalues(complex_diagonal_matrix))
print("Wektory własne:\n", matrix_eigenvectors(complex_diagonal_matrix))


