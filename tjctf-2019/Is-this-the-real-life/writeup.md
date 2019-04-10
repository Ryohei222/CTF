# Is this the real life (Crypto, 90pts)

ソースを見ると42行目辺りからの

```python
for c in range(len(flag)):
    nm = str(int(bin(int(flag[c].encode('hex'),16)).replace('0b', '')))
    for b in range(len(nm)):
        cipher[c] += int(nm[b])*nlist[b]
    cipher[c] = cipher[c]*int(nm)
    cipher[c] = cipher[c]%modulus
```

がつらそうだと感じます。

少し前に戻って```modulus```の定義を確認してみると、

```python
modulus = random_prime(2^floor(nbits/2)-1,lbound=2^floor(nbits/2-1),proof=False)
```

とあります。

sagemathのrandom_primeはlbound以上第一引数以下の素数を返す関数で、この場合だと512bitの素数が返されます。

さっきの

```python
cipher[c] = cipher[c]%modulus
```

で、```cipher[c]```の値は```modulus```より明らかに小さいので、この文は特に何もしていないことが分かります。

暗号化のところにコメントをつけると

```python
nm = str(int(bin(int(flag[c].encode('hex'),16)).replace('0b', ''))) # nmにはflag[c]のASCIIコードの2進数表現のstrが入る
for b in range(len(nm)):
    cipher[c] += int(nm[b])*nlist[b] # nm[b]は1か0
cipher[c] = cipher[c]*int(nm) # int(nm)はflag[c]のASCIIコードの2進数表現を10進数として読み取ったもの
```

こんな感じで、各文字は独立に暗号化されているので各文字ごとに```nm```の値を全探索すれば```flag```を復元することができます。len(cipher) \* ord('}') \* 8ステップぐらいで実行できます。
