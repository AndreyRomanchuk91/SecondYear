
def newton_Raphson(x0, e, N, f, df):
    print("\n\nNewton Raphson METHOD:")
    step = 1
    flag = 1
    condition = True
    while condition:
        if df(x0) == 0.0:  # Check if we divide by zero
            print("Error df(x0) is ZERO which causes us to divide by ZERO")
            break

        x1 = x0 - f(x0) / df(x0)  # The Newton Raphson pattern
        print("Iteration-%d, x1 = %0.6f and f(x1) = %0.6f" % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print("\nThe root is: %0.10f" % x1)
    else:
        print("\nTaylor tour does Not Converge")


if __name__ == '__main__':
    f = lambda x: x**3 - 3*x**2
    df = lambda x: 3*x**2 - 6*x
    x0 = 4
    TOL = 1e-6
    N = 100
    newton_Raphson(x0, TOL, N, f, df)