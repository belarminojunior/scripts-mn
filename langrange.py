X = [0, 1, 2, 3, 5, 6, 8]





mm = {}









########################################################################

def L(i):
    if mm.keys():
        mm.clear()
        
    C = [1]
    den = 1
    for j in range(len(X)):
        if i == j:
            continue

        num = [1, -X[j]]
        den *= X[i] - X[j]

        C = mult_pol(C, num)

    for j in range(len(C)):
        oC = C[j]
        C[j] /= den
    
        mm[C[j]] = str(oC) + "/" + str(den)
        
    return C



def mp(*pols):
    return mult_pol(pols)



def mult_pol(*pols):
    r = [1]
    for pol in pols:
        r = multiply_polynomials(r, pol)
    return r    
    
def multiply_polynomials(poly1, poly2):
    degree1 = len(poly1) - 1
    degree2 = len(poly2) - 1
    result_degree = degree1 + degree2
    result = [0] * (result_degree + 1)

    for i in range(degree1 + 1):
        for j in range(degree2 + 1):
            result[i + j] += poly1[i] * poly2[j]

    return result

