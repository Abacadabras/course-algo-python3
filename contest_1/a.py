"""Сложить два числа.

Формат входных данных
В строке последовательно вводятся два числа, которые нужно сложить.

Формат выходных данных
Одно число — результат."""


def foo_main() -> int:
    a, b = map(int, input().split())
    return a + b


if __name__ == '__main__':
    print(foo_main())
