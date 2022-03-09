
def king_step(n):
    res = [[1] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            res[i][j] = res[i-1][j] + res[i][j-1]

    return res


A = king_step(8)
for line in A:
    for element in line:
        print(f'{element:5}', end='')
    print()
