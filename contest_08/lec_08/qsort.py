from random import randint


def is_sorted(A):
    for _ in range(len(A)-1):
        if A[_] > A[_+1]:
            return False
    return True


def qsort(A: list, start=None, stop=None):

    if start is None:
        start = 0
    if stop is None:
        stop = len(A) - 1
    if stop - start < 1:
        return
    i = start
    j = stop
    while i < j:
        while A[i] < A[stop]:
            i += 1
        while j > 0 and A[j] >= A[stop]:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[stop], A[i] = A[i], A[stop]
    print('step :', start, i, stop, '\t', ' '.join(map(str, A)))
    qsort(A, start, i - 1)
    qsort(A, i + 1, stop)


A = [randint(10, 99) for _ in range(25)]
print('Start:\t\t', ' '.join(map(str, A)))
qsort(A)
print('Finish\t\t', ' '.join(map(str, A)))
print(is_sorted(A))
