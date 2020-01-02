#
# Fraction class:
#

class Fraction(object):
    """
    Class to represent a number as a fraction

    Examples: 1/2, 2/5
    """

    def __init__(self, n, d):
        """ Method to construct a Fraction object """
        # Check that n and d are of type int:
        if type(n) != int or type(d) != int:
            raise ValueError('requires type int')
        # Check that denominator is non-zero:
        if d == 0:
            raise ZeroDivisionError('requires non-zero denominator')
        # If we get here, n and d are ok => initialize Fraction:
        self.num = n
        self.denom = d

        # Call reduce() method
        self.reduce()

    def reduce(self):
        """
        Reduces self to simplest terms. This is done by dividing both
        numerator and denominator by their greatest common divisor (GCD).
        Also removes the signs if both numerator and denominator are
        negative. Whole numbers (1, 2, ...) are represented as
        1/1, 2/1, 3/1, ...
        """
        # Sign
        if self.num < 0:
            num_sign = -1
            self.num *= -1
        else:
            num_sign = 1

        if self.denom < 0:
            if num_sign == -1:
                denom_sign = 1
                num_sign = 1
            else:
                denom_sign = -1
            self.denom *= -1
        else:
            denom_sign = 1

        if self.num > self.denom:
            M = self.num
            N = self.denom
        else:
            M = self.denom
            N = self.num

        remainder = M % N
        while remainder != 0:
            M = N
            N = remainder
            remainder = M % N

        self.num //= N * num_sign
        self.denom //= N * denom_sign

    def adjust(self, factor):
        """ Multiplies numerator and denominator by factor. """
        # Adjust
        self.num *= factor
        self.denom *= factor

    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """ Returns new Fraction representing self * other """
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __add__(self, other):
        """ Returns new Fraction representing self + other """
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __float__(self):
        """ Returns a float-value of the Fraction object"""
        return self.num / self.denom  # result of / is of type float

