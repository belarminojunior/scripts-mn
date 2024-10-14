from math import *

FUNCTION = lambda x : exp(x-3) + x**2 - 5
A = 2
B = 3
MAX_ERROR = 0.01

print('k | ak | bk | c | e | sinal')

def bsc(f, a, b, e_max):
    e = 1
    it = 0
    while(e > e_max):
        c = (a + b) / 2
        e = (b - a) / 2
        print('{} | {} | {} | {} | {} | '.format(it, a, b, c, e), end = '')

        if f(a) * f(c) < 0:
            sg = '-'
            b = c
        elif f(a) * f(c) > 0:
            sg = '+'
            a = c

        print(sg)
        
        it += 1

bsc(FUNCTION, A, B, MAX_ERROR)