from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
from Crypto.Util.strxor import strxor
from netcat import Netcat
from time import sleep
import binascii

split = lambda s, n: [s[i:i+n] for i in range(0, len(s), n)]

welcome = b'''\
If you provide a message (besides this one) with
a valid message authentication code, I will give
you the flag.\x01\
If you provide a message (besides this one) with
a valid message authentication code, I will give
you the flag.'''
md = [b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07',
    b'If you provide a',
    b' message (beside',
    b's this one) with',
    b'\na valid message',
    b' authentication ',
    b'code, I will giv',
    b'e\nyou the flag.\x01']

nc = Netcat('54.159.113.26', 19002)
print('[+] ' + nc.read_until(b': ').decode('utf-8'))
mac = nc.read_until(b': ').decode('utf-8')
mac = binascii.unhexlify(mac[:64])
ivd = mac[:16]
t = mac[16:]
BLOCK_SIZE = 16
m = welcome
m = split(m, BLOCK_SIZE)
m[6] = strxor(t, strxor(md[0], ivd))
iv = strxor(long_to_bytes(14, BLOCK_SIZE), strxor(md[0], ivd))

m_united = b''
for mi in m:
    #print(mi)
    m_united = m_united + binascii.hexlify(mi)

assert len(binascii.unhexlify(binascii.hexlify(iv+t))) == 32

nc.write(m_united + b'\n')
print('[+] ' + nc.read_until(b': ').decode('utf-8'))
nc.write(binascii.hexlify(iv+t) + b'\n')
sleep(1)
flag = nc.read()
print('[+] ' + flag.decode('utf-8'))
# '''
m = pad(binascii.unhexlify(m_united), BLOCK_SIZE)
m = split(m, BLOCK_SIZE)
m.insert(0, long_to_bytes(len(m), BLOCK_SIZE))
assert strxor(m[0], iv) == strxor(md[0], ivd)
assert strxor(m[7], t) == strxor(ivd, md[0])
assert m[-1] == md[-1]
print(m)
# '''