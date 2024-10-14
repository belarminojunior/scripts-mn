X = [1980, 1990, 2000, 2010, 2020]
Y = [132165, 151326, 179323, 203302, 226542]
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
