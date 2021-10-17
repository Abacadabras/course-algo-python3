"""Длина удава
Требуется найти длину удава, выраженную в мартышках, попугаях или слоненках, по выбору пользователя. "Эффективная длина"
 попугая - 10см, мартышки - 90см, слоненка - 3м. Результат округляйте вниз, однако, если при этом получается ноль,
 выведите 1, чтобы не обижать удава.

Формат входных данных
В первой строке натуральное число - длина удава в сантиметрах. Во втрой строке - "в ком измерять", "monkey", "parrot"
или "elephant".

Формат выходных данных
Одно число — результат."""


from typing import Union


def foo_main() -> Union[int, str]:
    boa, k = int(input()), input()
    p = 10
    m = 90
    sl = 300
    if k == 'monkey':
        return max(1, boa // m)
    elif k == 'parrot':
        return max(1, boa // p)
    elif k == 'elephant':
        return max(1, boa // sl)
    else:
        return 'ERROR!'


if __name__ == '__main__':
    print(foo_main())
