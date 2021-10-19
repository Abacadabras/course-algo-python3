"""Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 10000 чисел (не
считая завершающего числа 0). Определите, сколько элементов этой последовательности равны ее наибольшему элементу
(включая сам наибольший). Числа, следующие за числом 0, считывать не нужно.

Формат входных данных
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).

Формат выходных данных
Выведите ответ на задачу (одно число)."""


def foo_main() -> int:

    max_number, number = float('-inf'), float('-inf')
    count_max_number = 0
    while number != 0:
        if max_number < number:
            max_number = number
            count_max_number = 1
        elif max_number == number:
            count_max_number += 1
        number = int(input())

    return count_max_number


if __name__ == '__main__':
    print(foo_main())
