from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util import Counter as counter
import codecs


class aes(object):
	"""docstring for aes"""
	username = None
	key = None
	sault = None

	def __init__(self, username, key, sault):
		super(aes, self).__init__()
		self.username = username
		self.key = key
		self.sault = sault
		self.key2key()

	def key2key(self):
		inputs = bytes(self.username + self.key + self.sault, 'utf-8')
		self.key = sha256(inputs)

	def encrypt(self, plain):
		co = counter.new(128)
		ci = AES.new(self.key, AES.MODE_CTR, counter = co)
		cipher = ci.encrypt(plain)
		return cipher

	def decrypt(self, cipher):
		co = counter.new(128)
		ci = AES.new(self.key, AES.MODE_CTR, counter = co)
		plain = ci.decrypt(cipher)
		return plain


def sha256(inputs):
	h = SHA256.new()
	if type(inputs) is str:
		inputs = bytes(inputs, 'utf-8')
	h.update(inputs)
	out = h.digest()
	return out






# test code

def aesTest():
	username = 'user'
	pw = 'pw'
	sault = '123'

	a = aes(username, pw, sault)
	cipher = a.encrypt('123')
	print(cipher)
	print(a.decrypt(cipher))


if __name__ == '__main__':
	pass
#	aesTest()
#	print(s)