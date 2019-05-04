from binascii import unhexlify
from math import gcd

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def encode(M, N, e=65537):
    C = pow(M, e, N)
    return C

def decode(C, d, N, e=65537):
    t = modinv(e, d)
    M = pow(C, t, N)
    M = unhexlify(hex(M)[2:])
    return M

def CommonModulusAttack(C1, C2, e1, e2, N):
    if gcd(e1, e2) != 1:
        assert('gcd(e1, e2) not equals to 1')
    s1, s2, _ = egcd(e1, e2)
    m = (pow(C1, s1, N) * pow(C2, s2, N) % 3