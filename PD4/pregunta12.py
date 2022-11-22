import numpy as np


def a(i, j):
    if j == 0:
        return 4
    elif (
        (j == i + 1 and i % 4 != 3)
        or (j == i - 1 and i % 4 != 0)
        or (j == i + 4 and i < 12)
        or (j == i - 4 and 3 < i < 16)
    ):
        return -1
    else:
        return 0


A = np.fromfunction(function=np.vectorize(a), shape=(16, 16), dtype=np.float64)
b = np.array(
    object=[
        1.902207,
        1.051143,
        1.175689,
        3.480083,
        0.819600,
        -0.264419,
        -0.412789,
        1.175689,
        0.913337,
        -0.150209,
        -0.264419,
        1.051143,
        1.966694,
        0.913337,
        0.819600,
        1.902207,
    ],
    dtype=np.float64,
).T


if __name__ == "__main__":
    print(f"A = \n{A}\n")
    (i, j) = (5, 1)
    print(f"a{i}{j} = ", A[i - 1][j - 1])
    from pregunta11 import is_symmetric, is_positive_definite

    print(f"La matriz A es definida positiva: {is_positive_definite(A)}.\n")
    print(f"La matriz A es simétrica: {is_symmetric(A)}.\n")
    A_tilde = A.T @ A
    b_tile = A.T @ b.T
    print(f"La matriz A_tilde es definida positiva: {is_positive_definite(A_tilde)}.\n")
    print(f"La matriz A_tilde es simétrica: {is_symmetric(A_tilde)}.\n")
# https://stackoverflow.com/a/24900335
# https://stackoverflow.com/a/16964006