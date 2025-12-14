import numpy as np

def perkalian_matriks_manual(X, Y):
    """
    Perkalian matriks manual
    X berukuran (m x n)
    Y berukuran (n x p)
    """

    # Ambil ukuran matriks
    m, n = X.shape
    n2, p = Y.shape

    # Validasi syarat perkalian matriks
    if n != n2:
        raise ValueError("Ukuran matriks tidak cocok untuk dikalikan")

    # Inisialisasi matriks hasil (m x p) dengan nol
    Z = np.zeros((m, p))

    # Proses perkalian manual (3 loop)
    for i in range(m):          # loop baris X
        for j in range(p):      # loop kolom Y
            for k in range(n):  # loop penjumlahan
                Z[i, j] += X[i, k] * Y[k, j]

    return Z


# =======================
# TEST CASE 1 (2x2)
# =======================

A1 = np.array([[1, 2],
               [3, 4]])

B1 = np.array([[5, 6],
               [7, 8]])

C1 = perkalian_matriks_manual(A1, B1)

print("TEST CASE 1")
print("Matriks A1:")
print(A1)
print("Matriks B1:")
print(B1)
print("Hasil A1 x B1:")
print(C1)

# Penjelasan:
# Baris 1 A1 x Kolom 1 B1: (1*5) + (2*7) = 5 + 14 = 19
# Baris 1 A1 x Kolom 2 B1: (1*6) + (2*8) = 6 + 16 = 22
# Baris 2 A1 x Kolom 1 B1: (3*5) + (4*7) = 15 + 28 = 43
# Baris 2 A1 x Kolom 2 B1: (3*6) + (4*8) = 18 + 32 = 50

# =======================
# TEST CASE 2 (2x3 x 3x2)
# =======================

A2 = np.array([[1, 2, 3],
               [4, 5, 6]])

B2 = np.array([[7, 8],
               [9, 10],
               [11, 12]])

C2 = perkalian_matriks_manual(A2, B2)

print("\nTEST CASE 2")
print("Matriks A2:")
print(A2)
print("Matriks B2:")
print(B2)
print("Hasil A2 x B2:")
print(C2)
# Penjelasan:
# Baris 1 A2 x Kolom 1 B2: (1*7) + (2*9) + (3*11) = 7 + 18 + 33 = 58
# Baris 1 A2 x Kolom 2 B2: (1*8) + (2*10) + (3*12) = 8 + 20 + 36 = 64
# Baris 2 A2 x Kolom 1 B2: (4*7) + (5*9) + (6*11) = 28 + 45 + 66 = 139
# Baris 2 A2 x Kolom 2 B2: (4*8) + (5*10) + (6*12) = 32 + 50 + 72 = 154

# =======================
# TEST CASE 3 (negatif & nol)
# =======================

A3 = np.array([[0, -1],
               [2, 3]])

B3 = np.array([[4, 5],
               [-6, 0]])

C3 = perkalian_matriks_manual(A3, B3)

print("\nTEST CASE 3")
print("Matriks A3:")
print(A3)
print("Matriks B3:")
print(B3)
print("Hasil A3 x B3:")
print(C3)
# Penjelasan:
# Baris 1 A3 x Kolom 1 B3: (0*4) + (-1*-6) = 0 + 6 = 6
# Baris 1 A3 x Kolom 2 B3: (0*5) + (-1*0) = 0 + 0 = 0
# Baris 2 A3 x Kolom 1 B3: (2*4) + (3*-6) = 8 - 18 = -10
# Baris 2 A3 x Kolom 2 B3: (2*5 ) + (3*0) = 10 + 0 = 10