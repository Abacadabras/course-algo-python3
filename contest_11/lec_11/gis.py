from random import randint


def gis(A: list):

    C = [0] * len(A)
    for i in range(len(A)):
        m = 0
        for j in range(i):
            if A[j] < A[i] and C[j] > m:
                m = C[j]
        C[i] = 1 + m

    return C, max(C)


if __name__ == '__main__':
    Z = [randint(10, 99) for _ in range(15)]
    print(Z)
    print(gis(Z))
