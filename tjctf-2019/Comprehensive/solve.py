m = 'tjctf{?????????????????}'.lower()
i_pre = [[225, 228, 219], [223, 220, 231], [205, 217, 224], [231, 228, 210], [208, 227, 220], [234, 236, 222], [232, 235, 227], [217, 223, 234]]

for k0 in range(ord('a'), ord('z') + 1):
    for k1 in range(ord('a'), ord('z') + 1):
        for k2 in range(ord('a'), ord('z') + 1):
            k = f'{chr(k0) + chr(k1) + chr(k2)}?????'
            i = []
            for x in i_pre:
                t = []
                for y in x:
                    t.append(y - k0)
                i.append(t)
            h = []
            for b in range(8):
                t = []
                for a in range(3):
                    t.append(ord(k[a]) ^ i[b][a])
                h.append(t)
            g = [a for a in range(24)]
            for x in range(3):
                for y in range(8):
                    g[x * 8 + y] = h[y][x]
            f = []
            for x in range(3):
                t = []
                for y in range(8):
                    t.append(g[x * 8 + y])
                f.append(t)
            if k0 ^ ord(m[0]) == f[0][0] and k1 ^ ord(m[1]) == f[0][1] and k2 ^ ord(m[2]) == f[0][2]:
                for k6 in range(ord('a'), ord('z') + 1):
                    k = chr(k0) + chr(k1) + chr(k2) + chr(f[0][3] ^ ord("t")) + chr(f[0][4] ^ ord("f")) + chr(f[0][5] ^ ord("{")) + chr(k6) + chr(f[2][7] ^ ord("}"))
                    m = ''
                    for x in range(3):
                        for y in range(8):
                            m += chr(f[x][y] ^ ord(k[y]))
                    if sum([ord(a) for a in m]) == 2613:
                        print(m)