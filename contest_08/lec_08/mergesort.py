from random import randint


def mergesort(A: list):

    if len(A) == 1:
        return
    n = len(A) // 2
    B = list(A[:n])
    C = list(A[n:])
    mergesort(B)
    mergesort(C)
    i = j = k = 0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1

    while i < len(B):
        A[k] = B[i]
        i += 1
        k += 1
    while j < len(C):
        A[k] = C[j]
        j += 1
        k += 1


X = [randint(10, 99) for _ in range(15)]
print(X)
mergesort(X)
print(X)
