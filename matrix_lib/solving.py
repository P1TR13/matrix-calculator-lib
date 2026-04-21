def Gauss (A, b):
    n = len(b)
    e = 10e-12
    for i in range(n):
        for j in range(i+1, n):
            for k in range(i, n):
                if abs(A[i][i]) < e:
                    raise ValueError("Can't divide by zero")
                m = -A[j][i] / A[i][i]
                A[j][k] += m * A[i][k]
    print(A)
    