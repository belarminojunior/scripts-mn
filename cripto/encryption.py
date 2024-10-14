import math

print("USAGE")
print("prsa(): To calculate RSA pqnq")
print("rsa(M, key, n): To encript or decript using RSA")

def ceasar(plain_text, k):
    encripted = ''
    for p in plain_text:
        encripted += chr((ord(p.lower()) - 97 + k) % 26 + 97)
    return encripted

def prsa():
    p = input_prime("p: ")
    q = input_prime("q: ")

    n = p * q
    print('n=', n)

    fi = (p-1)*(q-1)
    print('fi=', fi)

    while True:
        e = int(input('e: '))
        if e <= 3:
            print('e must be > 2')
            continue
        if gcf(e, fi) == 1:
            break
        else:
            print('has common factor with fi')

    d = inv_mod(e, fi)
    print('d=', d)

def rsa(M, key, n):
     
    for m in M:
        c = m**key % n
        print("{} -> {}".format(m, c))
        

    

# Helper Functions
def input_prime(msg):
    while True:
        n=int(input(msg))
        if is_prime(n):
            break
        print('not prime!')
        
    return n


def is_square(n):
    if n >= 0:
        sr = int(math.sqrt(n))
        return (sr * sr) == n
    return False

def inv_mod(A, M):
    m0 = M
    y = 0
    x = 1
 
    if (M == 1):
        return 0
 
    while (A > 1):
 
        # q is quotient
        q = A // M
 
        t = M
 
        # m is remainder now, process
        # same as Euclid's algo
        M = A % M
        A = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x

def gcf(a,b):
    (a,b) = (max(a,b),min(a,b))
    while b > 0:
        (a,b) = (b, a % b)
    return a

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def break_n(n, max_iterations=100):
    a = math.isqrt(n) + 1

    for i in range(max_iterations):
        b2 = a*a - n
        if is_square(b2):
            b = math.sqrt(b2)
            return int(a+b), int(a-b)
        a += 1
    return None
        
    
