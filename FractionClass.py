class Fraction:
    def __init__(self, numerator, denominator):
        # initialize
        self.numerator = numerator
        self.denominator = denominator
    
    def to_double(self):
        # returns double of decimal
        return self.numerator / self.denominator
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        lcm = self.denominator * other.denominator
        new_self_numerator = self.numerator * other.denominator
        new_other_numerator = other.numerator * self.denominator
        sum_numerator = new_self_numerator + new_other_numerator
        sum_denominator = lcm
        return Fraction(sum_numerator, sum_denominator)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __str__(self):
        thing = (str(self.numerator), str(self.denominator))
        return "/".join(thing)
    
    def __eq__(self, other):
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

def checks():
    frac = Fraction(1,2)
    frac2 = Fraction(2,8)
    num = 3

    print((frac + frac2) == Fraction(12, 16))
    print((frac2 + frac) == Fraction(12, 16))
    print((num + frac) == Fraction(7, 2))
    print((frac + num) == Fraction(7, 2))

checks()