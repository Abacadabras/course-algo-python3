from random import randint


def gcs(A: list, B: list) -> list:

    C = [[0] * (len(A) + 1) for _ in range(len(B)+1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                C[j][i] = C[j-1][i-1] + 1
            else:
                C[j][i] = max(C[j-1][i], C[j][i-1])

    return C


def get_cs(A: list, B: list, C: list) -> list:

    res = [0] * C[-1][-1]
    k = len(res) - 1
    i = len(A)
    j = len(B)
    while C[j][i] != 0:
        if C[j][i] - C[j-1][i-1] == 1 and A[i-1] == B[j-1]:
            res[k] = A[i-1]
            k -= 1
            i -= 1
            j -= 1
        else:
            if C[j-1][i] == C[j][i]:
                j -= 1
            else:
                i -= 1

    return res


if __name__ == '__main__':

    A = [randint(1, 5) for _ in range(15)]
    B = [randint(1, 5) for _ in range(12)]
    C = gcs(A, B)
    print('   ', *A)
    print(' ',  *C[0])
    for j in range(len(B)):
        print(B[j], *C[j+1])

    print(get_cs(A, B, C))
