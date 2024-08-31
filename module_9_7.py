"""Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
 и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three"""


def is_prime(func):
    def wrapper(*args):
        summa = func(*args)
        k = 0
        for i in range(2, int(summa ** 0.5) + 1):
                if summa % i == 0:
                    k = k + 1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return summa
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)