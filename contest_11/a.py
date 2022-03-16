"""A-Удалить короткие слова
Вводится строка, состоящая из слов, разделенных пробелами. Удалить из строки все слова, длина которых меньше пяти
символов. В строке не используются знаки препинания. Вывести суммы кодов букв слов, оставшихся после удаления (см.
функцию ord).

Формат входных данных
Строка со словами, разделенными пробелами.

Формат выходных данных
Последовательность суммы кодов. Гарантируется, что вывод не пустой."""


def foo_main(s: str):

    for word in s.split():
        if len(word) >= 5:
            sum_symbol = 0
            for symbol in word:
                sum_symbol += ord(symbol)
            print(sum_symbol, end=' ')


if __name__ == '__main__':
    s = input()
    foo_main(s)
