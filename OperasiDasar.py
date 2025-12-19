import numpy as np

# FUNGSI PENJUMLAHAN MATRIKS
def penjumlahan_matriks(A, B):
    """
    Menjumlahkan dua matriks 2x2
    Syarat: Ukuran matriks A dan B harus sama
    """
    return A + B

# FUNGSI PENGURANGAN MATRIKS
def pengurangan_matriks(A, B):
    """
    Mengurangkan matriks B dari matriks A
    """
    return A - B

# FUNGSI PERKALIAN MATRIKS
def perkalian_matriks(A, B):
    """
    Mengalikan dua matriks menggunakan perkalian matriks (dot product)
    """
    return np.dot(A, B)

# FUNGSI DETERMINAN MATRIKS
def determinan_matriks(A):
    """
    Menghitung determinan matriks 2x2
    Rumus manual 2x2:
    |a b|
    |c d|  = ad - bc
    """
    return np.linalg.det(A)

# FUNGSI INVERS MATRIKS
def invers_matriks(A):
    """
    Menghitung invers matriks jika determinan ≠ 0
    Jika determinan = 0, matriks tidak memiliki invers
    """
    det = np.linalg.det(A)
    if det == 0:
        return "Matriks tidak invertible (determinan = 0)"
    else:
        return np.linalg.inv(A)


# MATRIKS
A1 = np.array([[1, 2],
               [3, 4]])
B1 = np.array([[5, 6],
               [7, 8]])
A2 = np.array([[0, 0],
               [0, 0]])
B2 = np.array([[2, 3],
               [4, 5]])
A3 = np.array([[-1, 2],
               [3, -4]])
B3 = np.array([[4, -2],
               [-3, 1]])
A4 = np.array([[1, 2],
               [2, 4]])

# TEST CASE
print("=== TEST CASE PENJUMLAHAN MATRIKS ===")

# Test Case 1
print("Input:\n", A1, "\n+\n", B1)
print("Output:\n", penjumlahan_matriks(A1, B1))
# Penjelasan:
# Setiap elemen dijumlahkan sesuai posisinya

# Test Case 2
print("\nInput:\n", A2, "\n+\n", B2)
print("Output:\n", penjumlahan_matriks(A2, B2))
# Penjelasan:
# Matriks nol tidak mengubah nilai matriks lain

# Test Case 3
print("\nInput:\n", A3, "\n+\n", B3)
print("Output:\n", penjumlahan_matriks(A3, B3))
# Penjelasan:
# Bilangan negatif dan positif dijumlahkan normal


print("\n=== TEST CASE PENGURANGAN MATRIKS ===")

# Test Case 1
print("Input A:\n", A1)
print("Input B:\n", B1)
print("Output:\n", pengurangan_matriks(A1, B1))
# Penjelasan:
# Setiap elemen A dikurangi elemen B pada posisi yang sama

# Test Case 2
print("\nInput A:\n", B2)
print("Input B:\n", A2)
print("\nOutput:\n", pengurangan_matriks(B2, A2))
# Penjelasan:
# Mengurangi dengan matriks nol menghasilkan matriks itu sendiri

# Test Case 3
print("\nInput A:\n", A3)
print("Input B:\n", B3)
print("\nOutput:\n", pengurangan_matriks(A3, B3))
# Penjelasan:
# Operasi pengurangan berlaku untuk semua bilangan


print("\n=== TEST CASE PERKALIAN MATRIKS ===")

# Test Case 1
print("Input A:\n", A1)
print("Input B:\n", B1)
print("Output:\n", perkalian_matriks(A1, B1))
# Penjelasan:
# Perkalian baris matriks A dengan kolom matriks B

# Test Case 2
print("\nInput A:\n", A2)
print("Input B:\n", B2)
print("\nOutput:\n", perkalian_matriks(A2, B2))
# Penjelasan:
# Matriks nol dikali matriks apapun menghasilkan matriks nol

# Test Case 3
print("\nInput A:\n", A3)
print("Input B:\n", B3)
print("\nOutput:\n", perkalian_matriks(A3, B3))
# Penjelasan:
# Mengikuti aturan dot product matriks


print("\n=== TEST CASE DETERMINAN MATRIKS ===")

# Test Case 1
print("Input Matriks:\n", A1)
print("Determinant:", determinan_matriks(A1))
# Penjelasan:
# Determinan = (1*4) - (2*3) = -2

# Test Case 2
print("\nInput Matriks:\n", A4)
print("Determinant:", determinan_matriks(A4))
# Penjelasan:
# Baris saling bergantung → determinan = 0

# Test Case 3
print("\nInput Matriks:\n", A3)
print("Determinant:", determinan_matriks(A3))
# Penjelasan:
# Determinan ≠ 0, maka matriks invertible


print("\n=== TEST CASE INVERS MATRIKS ===")

# Test Case 1
print("Input Matriks:\n", A1)
print("Invers:\n", invers_matriks(A1))
# Penjelasan:
# Determinan ≠ 0, sehingga invers dapat dihitung

# Test Case 2
print("\nInput Matriks:\n", A4)
print("\nInvers:\n", invers_matriks(A4))
# Penjelasan:
# Determinan = 0 → tidak memiliki invers

# Test Case 3
print("\nInput Matriks:\n", A3)
print("\nInvers:\n", invers_matriks(A3))
# Penjelasan:
# Matriks memiliki invers karena determinan ≠ 0
