from math import gcd
from Crypto.Hash import SHA256
from binascii import unhexlify

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

if __name__ == '__main__':
    m = 'hoge'
    print(f'input "{m}"')
    h = SHA256.new()
    h.update(m)
    mh = int(h.hexdigest(), 16)
    N = int(input('input N:'))
    mhdash = int(input('input "wrong" signature:'))
    p = gcd(abs(mh - mhdash), N)
    q = N // p
    e = 65537
    C = int(input('input encrypted message'))
    flag = pow(C, modinv(e, (p - 1)*(q - 1)), N)
    print(unhexlify(hex(flag)))