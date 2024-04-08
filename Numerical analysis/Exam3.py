import numpy as np
from matrix_utility import *

def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points]  # Makes the initial matrix
    b = [[point[1]] for point in table_points]
    matrixSol = np.linalg.solve(matrix, b)

    result = sum([matrixSol[i][0] * (x ** i) for i in range(len(matrixSol))])
    print(f"\nThe Result of P(X={x}) is:")
    print(result)
    return result

def romberg_integration(func, a, b, n):
    counter = 1
    """
    Romberg Integration

    Parameters:
    func (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of iterations (higher value leads to better accuracy).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    h = b - a
    R = np.zeros((20, 20), dtype=float)

    R[0, 0] = 0.5 * h * (func(a) + func(b))

    for i in range(1, 20):
        h /= 2
        sum_term = 0
        counter += 1
        for k in range(1, 2 ** i, 2):
            sum_term += func(a + k * h)

        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_term

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4 ** j) - 1)

        if np.round(R[i - 1, i - 1], n) == np.round(R[i, i], n):
            #print(counter)
            return R[i, i]

    print("we have reach maximum iterations {20}")
    return R[n - 1, n - 1]


#Date:8.4.24
#Group members: Andrey Romanchuk 323694059;Shahar Dahan 207336355;Maya Rozenberg 313381600
#Source Git: https://github.com/lihiSabag/Numerical-Analysis-2023.git
#Private Git: https://github.com/AndreyRomanchuk91/SecondYear/tree/master/Numerical%20analysis
#Name: Andrey Romanchuk

def f(x):
    return (np.cos(x) + (x**3 - x + 2)) / (2 * np.e**(-x + 2))

if __name__ == '__main__':
    table_points = [(0.35, -3.5991), (0.4, -2.4416), (0.55, -0.9375), (0.65, 4.0256), (0.7, 2.6711)]
    x_a = 0.45
    x_b = 0.6
    polynomialInterpolation(table_points, x_a)
    polynomialInterpolation(table_points, x_b)
    a = -2.8
    b = 1.8
    n = 5
    integral = romberg_integration(f, a, b, n)
    print(f"Approximate integral in range [{a},{b}] is {integral}")
    n_new = 6
    integral = romberg_integration(f, a, b, n_new)
    print(f"Approximate integral in range [{a},{b}] is {integral}")