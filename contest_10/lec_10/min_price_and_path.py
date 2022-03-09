from random import randint


def min_prices1(n: int, price: list) -> list:

    res = [float("+inf"), price[0]] + [0] * (N - 1)
    for i in range(2, N + 1):
        res[i] = price[i - 1] + min(res[i - 1], res[i - 2])

    return res


def min_prices(n: int, price: list) -> list:

    res = [float('+inf')] * n
    res[0] = price[0]
    for i in range(n-1):
        if res[i+1] > res[i] + price[i+1]:
            res[i+1] = res[i] + price[i+1]
        if i+2 < n and res[i+2] > res[i] + price[i+2]:
            res[i+2] = res[i] + price[i+2]
    return res


def path(price: list, min_price: list) -> list:

    res = []
    i = len(price) - 1
    while i != 0:
        res.append(i)
        if min_price[i-1] == min_price[i] - price[i]:
            i -= 1
        else:
            i -= 2

    return [0] + res[::-1]


N = 12
prices = [randint(2, 10) for _ in range(N)]
print(prices)
min_p = min_prices(N, prices)
print(min_p)
print(min_prices1(N, prices))
print(path(prices, min_p))
