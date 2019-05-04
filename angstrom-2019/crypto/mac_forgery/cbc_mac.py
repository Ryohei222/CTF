from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
from Crypto.Util.strxor import strxor

split = lambda s, n: [s[i:i+n] for i in range(0, len(s), n)]

class CBC_MAC:

	BLOCK_SIZE = 16

	def __init__(self, key):
		self.key = key

	def next(self, t, m):
		return AES.new(self.key, AES.MODE_ECB).encrypt(strxor(t, m))

	def mac(self, m, iv):
		m = pad(m, self.BLOCK_SIZE)
		# hogehoge\x8\x8\x8\x8\x8\x8\x8\x8
		m = split(m, self.BLOCK_SIZE)
		# [fugafugafugafuga, hogehoge\x08\x08\x08\x0\x08\x08\x08\x08]
		m.insert(0, long_to_bytes(len(m), self.BLOCK_SIZE))
		# [\x00\x00\x00\x00...len(m), fugafugafugafuga, hogehoge\x08\x08\x08\x0\x08\x08\x08\x08]
		t = iv
		for i in range(len(m)):
			t = self.next(t, m[i])
		return t

	def generate(self, m):
		iv = get_random_bytes(self.BLOCK_SIZE)
		return iv, self.mac(m, iv)

	def verify(self, m, iv, t):
		return self.mac(m, iv) == t
