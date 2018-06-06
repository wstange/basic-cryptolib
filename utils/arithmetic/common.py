# extended greatest common divisor
def egcd(a, b):
	if a < 0: a = a%b
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)


# greatest common divisor
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
