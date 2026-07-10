# -*- coding: utf-8 -*-
# @Time    : 2026/7/11 2:57
# @Author  : listem
# @FileName: recursive_func.py
# @Software: PyCharm

def sum_digits(n):
    if n < 10:
        return n

    else:
        all_but_last, last = n // 10, n % 10

        return sum_digits(all_but_last) + last


print(sum_digits(9))
print(sum_digits(18117))
print(sum_digits(9437184))
print(sum_digits(11408855402054064613470328848384))


def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact_iter(4))
print(fact(4))
