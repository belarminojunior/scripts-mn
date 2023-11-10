from math import *

FUNCTION = lambda x, y : -x*y
x0 = 0
y0 = 1
xn = 0.5
h = 0.1

def e(f, x0, y0, xn, h):
    k = 0
    print('k | xk | yk')

    xk = x0
    yk = y0
    
    while True:
        print('{:.5f} | {:.5f} | {:.5f}'.format(k, xk, yk))

        yk = yk + h * f(xk, yk)
        xk = xk + h
        k += 1

        if xk > xn:
            break

e(FUNCTION, x0, y0, xn, h)
