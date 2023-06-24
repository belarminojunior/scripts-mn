from math import *

FUNCTION = lambda x : x**2 - 5
A = 2
B = 3
MAX_ERROR = 0.1

def bsc(f, a, b, e_max):
    e = 1
    it = 1
    while(e > e_max):
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            sg = '-'
            b = c
        elif f(a) * f(c) > 0:
            sg = '+'
            a = c
        e = (b - a) / 2

        print('{} | {} | {} | {} | {} | {}'.format(it, a, b, c, sg, e))
        it += 1

bsc(FUNCTION, A, B, MAX_ERROR)