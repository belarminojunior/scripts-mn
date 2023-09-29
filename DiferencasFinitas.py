X = [1.34, 1.44, 1.54, 1.64, 1.74]
Y = [1.38, 1.62, 1.87, 2.14, 2.42]
CASAS_DECIMAIS = 2










from math import *
M = [[], []]
M[0] = [a for a in X]
M[1] = [a for a in Y]

for i in range(2, len(X)+1):
    row = []
    for j in range(len(X)-i+1):
        row.append(0)
    M.append(row)


for i in range(2, len(M)):
    for j in range(len(M[i-1]) - 1):
        M[i][j] = round(M[i-1][j+1] - M[i-1][j], CASAS_DECIMAIS)


for row in M:
    print(row)
