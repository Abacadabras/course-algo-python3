from math import log


def foo_main(n: int) -> int:

    max_number = int((n+6)*(log(n)+log(log(n))))
    eratos = [True] * max_number
    eratos[0] = eratos[1] = False
    ch = 0
    for i in range(2, max_number):
        if eratos[i]:
            for j in range(2*i, max_number, i):
                eratos[j] = False
            ch += 1
            if ch == n:
                return i


if __name__ == '__main__':
    number1 = int(input())
    print(foo_main(number1))
