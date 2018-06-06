

##
#   This class bundle all the mathematical needed functions
#
class KryptoMath:


    ##
    #   greatest common divisor
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    ##
    #   extended greatest common divisor
    def egcd(self, a, b):
        if a < 0:
            a = a % b
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    ##
    #   modular inverses
    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
