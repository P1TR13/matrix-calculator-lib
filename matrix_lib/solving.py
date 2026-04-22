def Gauss (A, b):
    A = [row[:] for row in A]
    b = b[:]
    
    n = len(b)
    e = 1e-12
    for i in range(n):
        for j in range(i+1, n):
            m = -A[j][i] / A[i][i]
            b[j] += m * b[i]
            for k in range(i, n):
                if abs(A[i][i]) < e:
                    raise ValueError("Can't divide by zero")
                
                A[j][k] += m * A[i][k]
    
    for i in range(n-1, -1, -1):
        sum = b[i]
        for j in range(i+1, n):
            sum -= A[i][j] * b[j]
            if abs(A[i][i]) < e:
                return False
        b[i] = sum/A[i][i]
    return b

