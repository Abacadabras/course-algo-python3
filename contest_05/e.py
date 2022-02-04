"""На вход подаётся массив значений функции. Требуется вывести положения (индексы) строгих локальных минимумов и
локальных максимумов.

Формат входных данных
Первая строка: N -- число элементов в массиве (2 < N < 100000). Вторая строка: N чисел -- элементы массива.

Формат выходных данных
Все индексы локальных экстремумов одной строкой."""


def foo_main(n: int) -> list:

    result = []
    arr = list(map(int, input().split()))
    for i in range(1, n-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            result.append(i)
        elif arr[i-1] > arr[i] < arr[i+1]:
            result.append(i)

    return result


if __name__ == '__main__':
    n1 = int(input())
    print(*foo_main(n1))
