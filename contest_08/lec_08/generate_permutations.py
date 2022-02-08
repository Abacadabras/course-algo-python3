
def generate_permutations(N: int, M:int=-1, prefix=None, used=None):
    """Генерация всех перестановок N чисел в M позициях, с префиксом prefix, N < M, без незначащего нуля"""

    prefix = prefix or []
    used = used or [False]*(N+1)
    M = N if M == -1 or N < M else M
    if M == 0:
        print(*prefix, end=', ', sep='')
        return
    for digit in range(1, N+1):
        if not used[digit]:
            used[digit] = True
            prefix.append(digit)
            generate_permutations(N, M-1, prefix, used)
            prefix.pop()
            used[digit] = False


generate_permutations(5)
