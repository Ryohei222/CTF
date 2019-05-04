def encrypt(d, s):
    e = ''
    for c in d:
        e += chr((ord(c)+s) % 0xff)
    return e

encrypted = ':<M?TLH8<A:KFBG@V'

for i in range(0xff):
    decrypted = ''
    for c in encrypted:
        decrypted += chr((ord(c) - i) % 0xff)
    print(decrypted)