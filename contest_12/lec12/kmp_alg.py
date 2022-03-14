from pref import pref


def kmp(subs: str, S: str) -> list:

    S1 = subs + '\0' + S
    P = pref(S1)
    print(*S1)
    print(*P)

    res= []
    n = len(subs)
    for i in range(2 * n, len(S1)):
        if P[i] == n:
            res.append(i - 2*n)
    return res


if __name__ == "__main__":
    print(kmp('aba', 'abacabadabacabac'))
