from random import randint, random


def mp(weights: list, price: list, W: int) -> list:

    R = [[0.0] * (W+1) for _ in range(len(weights) + 1)]
    for i in range(1, W + 1):
        for j in range(1, len(weights) + 1):
            if weights[j-1] > i:
                R[j][i] = R[j-1][i]
            else:
                R[j][i] = max(R[j-1][i], price[j-1] + R[j-1][i-weights[j-1]])
    return R  # R[-1][-1] - result


if __name__ == '__main__':
    weights = [randint(1, 5) for _ in range(10)]
    price = [random() + 0.1 for _ in range(10)]

    R = mp(weights, price, 20)

    print(weights)
    print(price)
    print(' ',' '.join(map(lambda x: f'{x:>4}', range(21))))
    for j in range(11):
        print(j, *map(lambda x: f'{x:0.02f}', R[j]))
