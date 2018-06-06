import common


def modinv(a, m):
	g, x, y = common.egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m
