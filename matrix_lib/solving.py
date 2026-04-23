def Gauss (A, b):
    A = [row[:] for row in A]
    b = b[:]

    n = len(b)
    e = 1e-12
    for i in range(n):
        if abs(A[i][i]) < e:
            if abs(b[i]) > e:
                return {'error': 'no_solution'}
            else:
                return {'error': 'infinite_solutions'}
        
        for j in range(i + 1, n):
            m = -A[j][i] / A[i][i]
            b[j] += m * b[i]
            for k in range(i, n):
                A[j][k] += m * A[i][k]
    
    for i in range(n - 1, -1, -1):
        sum_val = b[i]
        for j in range(i + 1, n):
            sum_val -= A[i][j] * b[j]
        
        if abs(A[i][i]) < e:
            if abs(sum_val) > e:
                return {'error': 'no_solution'}
            else:
                return {'error': 'infinite_solutions'}
        
        b[i] = sum_val / A[i][i]
    
    return b

