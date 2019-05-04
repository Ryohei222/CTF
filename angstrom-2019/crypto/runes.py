from phe import paillier
from binascii import unhexlify
from math import gcd
import sys

sys.setrecursionlimit(100000)

p = 310013024566643256138761337388255591613
q = 319848228152346890121384041219876391791
n = p * q
g = 99157116611790833573985267443453374677300242114595736901854871276546481648884
c = 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869
k = 1
l = ((p - 1) * (q - 1)) // gcd(p - 1, q - 1)

pk = paillier.PaillierPublicKey(n)
pp = paillier.PaillierPrivateKey(pk, p, q)
en = paillier.EncryptedNumber(pk, c)
m = pp.decrypt(en)
print(unhexlify(hex(m)[2:]))

#m = div(pow(c, l, n * n), pow(g, l, n * n))

'''
[msieve153] > .\msieve153.exe -q -v 99157116611790833573985267443453374677300242114595736901854871276546481648883

Msieve v. 1.53 (SVN 1005)
Sat Apr 20 10:47:37 2019
random seeds: b3564e14 fdbd8498
factoring 99157116611790833573985267443453374677300242114595736901854871276546481648883 (77 digits)
searching for 15-digit factors
commencing quadratic sieve (77-digit input)
using multiplier of 3
using generic 32kb sieve core
sieve interval: 12 blocks of size 32768
processing polynomials in batches of 17
using a sieve bound of 922073 (36471 primes)
using large prime bound of 92207300 (26 bits)
using trial factoring cutoff of 26 bits
polynomial 'A' values have 10 factors

sieving in progress (press Ctrl-C to pause)
36843 relations (19478 full + 17365 combined from 190428 partial), need 36567
36843 relations (19478 full + 17365 combined from 190428 partial), need 36567
sieving complete, commencing postprocessing
begin with 209906 relations
reduce to 52041 relations in 2 passes
attempting to read 52041 relations
recovered 52041 relations
recovered 38625 polynomials
attempting to build 36843 cycles
found 36843 cycles in 1 passes
distribution of cycle lengths:
   length 1 : 19478
   length 2 : 17365
largest cycle: 2 relations
matrix is 36471 x 36843 (5.4 MB) with weight 1114324 (30.25/col)
sparse part has weight 1114324 (30.25/col)
filtering completed in 3 passes
matrix is 25048 x 25112 (4.0 MB) with weight 848819 (33.80/col)
sparse part has weight 848819 (33.80/col)
saving the first 48 matrix rows for later
matrix includes 64 packed rows
matrix is 25000 x 25112 (2.7 MB) with weight 623329 (24.82/col)
sparse part has weight 453631 (18.06/col)
commencing Lanczos iteration
memory use: 2.7 MB
lanczos halted after 397 iterations (dim = 24996)
recovered 16 nontrivial dependencies
p39 factor: 310013024566643256138761337388255591613
p39 factor: 319848228152346890121384041219876391791
elapsed time 00:01:57
'''