encrypted = "1m__s4sk_s3np41m1r_836lly_cut3_34799u14}1osenCTF{5sKm"
L = len(encrypted)

for a in range(0, L + 1):
    for b in range(0, L + 1):
        if a == b:
            continue
        for k in range(1, L + 1):
            decrypted = list(encrypted)
            i = k
            for _ in range(L):
                i = (i - k) % L
                s = (i + a) % L
                t = (i + b) % L
                decrypted[t], decrypted[s] = decrypted[s], decrypted[t]
            if "".join(decrypted)[0:9] == "KosenCTF{":
                print("".join(decrypted))
