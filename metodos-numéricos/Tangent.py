from math import *

FUNCTION = lambda x : x**2 - 5
DERIVATIVE = lambda x : 2 * x
x0 = 3
MAX_ERROR = 0.01

def tg(f, ff, x0, erro_max):
    m = 0
    xm = x0

    print('m | xm | xmm | erro')
    while True:
        #FC
        xmm = xm - (f(xm) / ff(xm))
        e = abs(xmm - xm)

        print('{} | {:.6f} | {:.6f} | {:.6f}'.format(m, xm, xmm, e))

        m += 1
        xm = xmm
        if e < erro_max:
            break

tg(FUNCTION, DERIVATIVE, x0, MAX_ERROR)
