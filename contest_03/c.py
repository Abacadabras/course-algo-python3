"""Разложите неотрицательное целое десятичное число по степеням основания.

Слагаемое разложение должно быть записано слитно в формате: цифра*10^разряд . Слагаемые разделяются тремя символами:
 + (пробел, знак плюс, пробел). Слагаемые должны располагаться по убыванию разряда.

Формат входных данных
Нетрицательное целое десятичное число.

Формат выходных данных
Одна строка."""


def foo_main() -> str:

    number = input()
    length = len(number) - 1
    power = '*10^'
    separator = ' + '
    result = ''
    for ind in range(length + 1):
        print(number[ind], power, length - ind, sep='', end='')
        if length - ind != 0:
            print(separator, sep='', end='')
    return result


if __name__ == '__main__':
    print(foo_main())
