X = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
Y = [0.84147, 0.81019, 0.77670, 0.74120, 0.70389, 0.66500, 0.62473]
N = 6

H = (X[len(X) - 1] - X[0]) / N

def metodo_trapezio(Y, H):
    return (H/2) * (Y[0] + Y[len(Y) - 1] + 2 * sum(Y[1:len(Y) - 1]))

print("Resposta =", metodo_trapezio(Y, H))