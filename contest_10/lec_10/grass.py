from random import randint


def grass1(n: int, free: list) -> list:

    res = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        if free[i-1]:
            res[i] = res[i-1] + res[i-2]
    return res


def grass(n: int, free: list) -> list:

    A = [0] * n
    A[0] = 1
    for i in range(n-1):
        if i+1 < n and free[i+1]:
            A[i+1] += A[i]
        if i+2 < n and free[i+2]:
            A[i+2] += A[i]

    return A


N = 10  
allowed = [True] * N

allowed[randint(1, N-2)] = False
print(allowed)
print(grass(N, allowed))
print(grass1(N, allowed))
