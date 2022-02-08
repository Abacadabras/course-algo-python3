"""Требуется определить, является ли данный год високосным. (Год является високосным, если его номер кратен 4,
но не кратен 100, а также если он кратен 400).

Формат входных данных
На вход подается натуральное число N - номер года (0 < N < 100000).

Формат выходных данных
Вывести YES если год високосный и NO в противном случае"""


def foo_main(n: int) -> str:

    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return "YES"
    return "NO"


if __name__ == '__main__':
    n1 = int(input())
    print(foo_main(n1))