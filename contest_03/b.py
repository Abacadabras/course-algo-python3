"""Главный врач хочет проанализировать статические данные потока поступающих пациентов. Он хочет увидеть среднюю
арифметическую температуру пациентов от 60 лет и выше, а также пациентов, вес которых отклоняется от нормального больше,
 чем на 10 килограмм. Нормальным весом в килограммах считать рост за вычетом ста сантиметров. Если таких пациентов нет -
  вывести ноль.

Формат входных данных
На вход алгоритм получает количество строк N, а затем N строк. В каждой строке по 4 числа, разделённых табуляцией:
age height weight temperature

Формат выходных данных
Одно вещественное число. Точность проверки - 5 знаков после запятой."""


def foo_main() -> float:

    sum_numbers, count_numbers = 0, 0
    count = int(input())

    for _ in range(count):
        age, height, weight, temperature = map(float, input().split())
        if age >= 60 or abs(weight - (height-100)) > 10:
            sum_numbers += temperature
            count_numbers += 1
    return 0 if sum_numbers == 0 else round(sum_numbers/count_numbers, 5)


if __name__ == '__main__':
    print(foo_main())
