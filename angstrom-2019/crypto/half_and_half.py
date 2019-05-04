# from secret import flag
def xor(x, y):
    o = ''
    for i in range(len(x)):
        o += chr(ord(x[i])^ord(y[i]))
    return o

# assert len(flag) % 2 == 0
# half = len(flag)//2
# milk = flag[:half]  # actf{???????
# cream = flag[half:] # ???????????}

C = '\x15\x02\x07\x12\x1e\x100\x01\t\n\x01"'
print('actf{coffee' + xor('}', C[11]) + xor('actf{coffee', C) + '}')

# s = '\x100\x01\t\n\x01'
# print(xor('coffee', s))