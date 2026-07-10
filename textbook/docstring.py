# -*- coding: utf-8 -*-
# @Time    : 2026/7/9 2:49
# @Author  : listem
# @FileName: docstring.py.py
# @Software: PyCharm

def pressure(v, t, n=6.022e23):
    """计算理想气体的压力（单位：帕斯卡）

    使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- 气体体积，单位：立方米
    t -- 绝对温度，单位：开尔文
    n -- 气体粒子数
    """
    k = 1.38e-23  # 玻尔兹曼常数
    return n * k * t / v


help(pressure)
print(pressure(1, 273.15))
print(pressure(1, 273.15, 3 * 6.022e23))


def absolute_value(x):
    """Compute abs(x)."""
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x


result = absolute_value(-2)
print(result)


def fib(n):
    pred, curr = 0, 1
    if n == 1:
        return pred
    k = 2
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1

    return curr


for i in range(1, 10):
    print(fib(i), end=" ")

assert fib(8) == 13

assert fib(50) == 7778742049
print()


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def cube(x):
    return x * x * x


def identity(x):
    return x


def pi_term(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))


def pi_sum(n):
    return summation(n, pi_term)


def sum_cubes(n):
    return summation(n, cube)


def sum_naturals(n):
    return summation(n, identity)


print(sum_naturals(10))
print(sum_cubes(3))
print(pi_sum(1e6))
