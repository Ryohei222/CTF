import lxml.html
import requests
from binascii import hexlify, unhexlify

def post_result(result):
    url = 'http://crypto.kosenctf.com:8000/result'
    cookies = {'result': result.decode('utf-8')}
    r = requests.get(url, cookies=cookies)
    return r.text

def make_result(iv, cipher):
    assert len(iv) == 16, "Error: invaild iv length"
    assert len(cipher) % 16 == 0, "Error: invaild ciphertext length"
    return hexlify(iv+cipher)

def is_valid_padding(target, decrypted_bytes, attempt_byte, attempt_idx):
    # attempt_idx -> 1-indexed
    attempt_bytes = b'\x00' * (16-attempt_idx) + (attempt_byte).to_bytes(1, 'big')
    adjusted_bytes = b''
    for c in decrypted_bytes:
        adjusted_bytes += (int.from_bytes(c, byteorder='big') ^ attempt_idx).to_bytes(1, 'big')
    result = make_result(attempt_bytes+adjusted_bytes, target)
    return not (post_result(result)[:10] ==  "ERROR: padding error"[:10])

def xor(b1, b2):
    res = b''
    for i in range(len(b1)):
        a1 = int.from_bytes(b1[i], byteorder='big')
        a2 = b2[i]
        res = res + (a1 ^ a2).to_bytes(1, 'big')
    return res

result = b'\x02:\x9a\x1f[\xe5*\xd9H\x90b\xa6d]\xbf2O\x92\x9d\xa2\x925\x1c\xaa\xad\x8a\xd3\xff\x12\xccSS\xaeka\xe3?\xeb?1\xad]%\x95\xa3\xdc\xf1\xbfm2\xa3\xbe\xe2\xec&+\xd3\xff\n>\xcc\x1ef\xc5'
iv = result[:16]
c = [result[i:i+16] for i in range(16, len(result), 16)]
M = [
    b'{"is_hit": true,',
    b' "number": 76587',
    b'6346283}'+b'\x08'*8
]
c.reverse()

for i in range(len(c)):
    target = c[i]
    prev = c[i + 1] if i != len(c) - 1 else iv
    decrypted_bytes = []
    attempt_byte = 0
    attempt_idx = 1
    while True:
        assert attempt_byte <= 0xff, "Not Found Byte"
        if is_valid_padding(target, decrypted_bytes, attempt_byte, attempt_idx):
            decrypted_bytes.insert(0, (attempt_idx ^ attempt_byte).to_bytes(1, 'big'))
            attempt_idx += 1
            attempt_byte = 0
            if attempt_idx <= 16:
                continue
            else:
                break
        else:
            attempt_byte += 1
    if i != len(c) - 1:
        c[i + 1] = xor(decrypted_bytes, M[len(M) - i - 1])
        print(f'[+] Dec(C[{len(c) - i - 1}]) is {c[i + 1]}')
    else:
        iv = xor(decrypted_bytes, M[len(M) - i - 1])
        print(f'[+] iv is {iv}')
c.reverse()

ci = b''
for x in c:
    ci = ci + x
print(f'cookie is {make_result(iv, ci)}')