from math import *

FUNCTION = lambda x: x*x - 5
x0 = 2
xf = 3
MAX_ERROR = 0.01

def sc(f, x0, xf, erro_max):
    m = 0
    xm = x0

    print('m | xm | xmm | erro')
    while True:
        #FC
        xmm = (xf * f(xm) - xm * f(xf)) / (f(xm) - f(xf))
        e = abs(xmm - xm)

        print('{} | {:.6f} | {:.6f} | {:.6f}'.format(m, xm, xmm, e))

        m += 1
        xm = xmm
        if e < erro_max:
            break

sc(FUNCTION, x0, xf, MAX_ERROR)