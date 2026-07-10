# -*- coding: utf-8 -*-
# @Time    : 2026/7/10 18:49
# @Author  : listem
# @FileName: decorator_underst.py
# @Software: PyCharm

"""
函数也是对象 (First-class Object)
可以从c的角度实现这个函数是一等公民的例子

函数拥有和变量一样的一切性质

为什么叫装饰器，因为只是外面包了一层

"""


def hello():
    print("hello")


def run(fn):
    fn()


def make():
    def hello():
        print("Hello")

    return hello


hello()
print(hello)

# assignment
f = hello
f()
hello()

# 函数作为argument
run(hello)

# 函数作为return value
f = make()
f()


# 实现打印功能 在不改变原函数状态的情况下给函数增加新功能

def deco(fn):
    def wrapped():
        print("start")
        fn()
        print("end")

    return wrapped


@deco  # hello_1 = deco(hello_1)
def hello_1():
    print("hello_1")


print()

hello = deco(hello)
hello()
print()
hello_1()

# 实现用装饰器统计程序运行时间
import time


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


# def prime_nums():
#     t1 = time.time()
#     for i in range(2, 10000):
#         if is_prime(i):
#             print(i)
#     t2 = time.time()
#     print(t2 - t1)


def prime_nums():
    for i in range(2, 10000):
        if is_prime(i):
            print(i)




def display_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2 - t1)

    return wrapper

@display_time
def prime_nums_dec():
    for i in range(2, 10000):
        if is_prime(i):
            print(i)


# prime_nums()

prime_nums = display_time(prime_nums)
prime_nums()
print()
prime_nums_dec()