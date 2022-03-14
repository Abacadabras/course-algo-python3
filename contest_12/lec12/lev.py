
def lev(s: str, g: str) -> list:

    L = [[i+j if i*j == 0 else 0 for j in range(len(s) + 1)] for i in range(len(g) + 1)]

    for i in range(1, len(g) + 1):
        for j in range(1, len(s) + 1):
            if s[j-1] == g[i-1]:
                L[i][j] = L[i-1][j-1]
            else:
                L[i][j] = min(L[i-1][j], L[i-1][j-1], L[i][j-1]) + 1
    return L


def get_chahges(s: str, g: str) -> list:
    """git list of levenshtain changes"""
    L = lev(s, g)
    res = [0] * L[-1][-1]
    k = len(res) - 1
    i = len(g)
    j = len(s)
    while i + j != 0:
        if s[i-1] == g[i-1] and L[i][j] == L[i-1][j-1]:
            i -= 1
            j -= 1
        else:
            if L[i-1][j] - L[i-1][j] == 1:
                res[k] = f'insert {g[i-1]} in pos {i-1}'
            elif L[i][j] - L[i][j-1] == 1:
                res[k] = f'delete {s[j-1]} in pos {j-1}'
                k -= 1
                j -= 1
            else:
                res[k] = f'exchange {s[j-1]}({j-1}) on {g[i-1]}({i-1})'
                k -= 1
                i -= 1
                j -= 1
    return res


if __name__ == "__main__":
    S = 'kolbaca'
    G = 'moloko'
    L = lev(S, G)
    print('   ', *S)
    print(' ', *L[0])
    for i in range(len(G)):
        print(G[i], *L[i+1])

    A = get_chahges(S, G)
    for line in A:
        print(line)
