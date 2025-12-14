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
# CONTOH PENGUJIAN
# =======================

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C_manual = perkalian_matriks_manual(A, B)

print("Matriks A:")
print(A)

print("\nMatriks B:")
print(B)

print("\nHasil perkalian manual A x B:")
print(C_manual)
