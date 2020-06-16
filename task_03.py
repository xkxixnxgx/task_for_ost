# Задача.
# Написать функцию, которая возвращает количество идущих подряд нулей на конце n!.

# импортируем функцию для расчета факториала из стандартного модуля math
from math import factorial

# решение на основе анализа последних символов, на которые заканчивается факториал от заданного числа
def get_zeros(n):
    fact_n_str = str(factorial(n))
    x = 0
    while fact_n_str[-1] == '0':
        fact_n_str = fact_n_str[0:-1]
        x += 1
    return int(x)


if __name__ == '__main__':
    n = int(input())
    print(get_zeros(n))
