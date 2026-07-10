# -*- coding: utf-8 -*-
# @Time    : 2026/7/10 18:22
# @Author  : listem
# @FileName: decorator.py
# @Software: PyCharm

"""
triple = trace(triple)
triple()

triple_dec(12)
"""

def trace(fn):
    def wrapped(x):
        print("->", fn, '(', x, ')')
        return fn(x)

    return wrapped


def triple(x):
    return 3 * x


@trace
def triple_dec(x):
    return 3 * x


triple = trace(triple)
print(triple(12))
triple_dec(12)
