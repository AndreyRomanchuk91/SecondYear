import numpy as np
from numpy.linalg import norm

from matrix_utility import is_diagonally_dominant, is_square_matrix, DominantDiagonalFix


def gauss_seidel(A, b, X0, TOL=1e-16, N=200):
    n = len(A)
    k = 1

    # Check if matrix A is square
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be a square matrix")

    # Check if matrix A is diagonally dominant, if not, attempt to fix it
    if not is_diagonally_dominant(A):
        A, b = DominantDiagonalFix(A, b)
        print("Matrix is not diagonally dominant - Fixed matrix using DominantDiagonalFix")

    print(
        "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")

    x = np.zeros(n, dtype=np.double)

    while k <= N:
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if np.linalg.norm(x - X0, np.inf) < TOL:
            print("Converged to solution within tolerance")
            return tuple(round(val, 2) for val in x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(round(val, 2) for val in x)


if __name__ == '__main__':

    A = np.array([[1, 1, 1], [1, 2, 4], [1, 3, 9]])
    b = np.array([3, 4, -1])
    X0 = np.zeros_like(b)

    solution =gauss_seidel(A, b, X0)
    print("\nApproximate solution:", solution)