import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):

        # Calculate U
        for k in range(i, n):
            sum_upper = 0

            for j in range(i):
                sum_upper += L[i][j] * U[j][k]

            U[i][k] = A[i][k] - sum_upper

        # Diagonal of L is 1
        L[i][i] = 1

        # Calculate L
        for k in range(i + 1, n):
            sum_lower = 0

            for j in range(i):
                sum_lower += L[k][j] * U[j][i]

            L[k][i] = (A[k][i] - sum_lower) / U[i][i]

    return L, U


def forward_substitution(L, b):
    n = len(L)
    y = np.zeros(n)

    for i in range(n):
        sum_value = 0

        for j in range(i):
            sum_value += L[i][j] * y[j]

        y[i] = b[i] - sum_value

    return y


def backward_substitution(U, y):
    n = len(U)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        sum_value = 0

        for j in range(i + 1, n):
            sum_value += U[i][j] * x[j]

        x[i] = (y[i] - sum_value) / U[i][i]

    return x


# Input Matrix A
A = np.array([
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
], dtype=float)

# Constant Matrix b
b = np.array([-2, 9, -5], dtype=float)

# Perform LU Decomposition
L, U = lu_decomposition(A)

# Solve Ly = b
y = forward_substitution(L, b)

# Solve Ux = y
x = backward_substitution(U, y)

# Display Results
print("Matrix A:")
print(A)

print("\nLower Triangular Matrix L:")  
print(L)

print("\nUpper Triangular Matrix U:")
print(U)

print("\nIntermediate Solution y:")
print(y)

print("\nFinal Solution x:")
print(x)
