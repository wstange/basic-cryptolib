from utils.arithmetic import common


##
# compute the modular inverse of a number and his modulus
#
def modinv(a, m):
	g, x, y = common.egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m
