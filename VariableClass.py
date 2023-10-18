import math

class Variable: # for the independent variables
    def __init__(self, name=None):
        self.name = name

    # The evaluation method for independent variables, base case
    def evaluate(self, values): 
        # values will be a dictionary that looks like: {"x_1": 3, "x_2": -4}
        return values[self.name]
    
    def __add__(self, other):
        return AdditionVariable(self, other)
    
    def __radd__(self, other):
        return AdditionVariable(self, other)
    
    def __sub__(self, other):
        return self + other * (-1)
    
    def __rsub__(self, other):
        return self + other * (-1)

    def __mul__(self, other):
        return MultiplicationVariable(self, other)
    
    def __rmul__(self, other):
        return MultiplicationVariable(self, other)
    
    def __pow__(self, other):
        return PowerVariable(self, other)
    
    def __truediv__(self, other):
        return self * (other ** -1)

    @staticmethod
    def exp(other):
        return e ** other.evaluate(values)

    @staticmethod
    def log(other):
        return math.log(other.evaluate(values))
    
class AdditionVariable(Variable):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # override the evaluate method (recursive step)
    def evaluate(self, values):
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) + self.right
        return self.left.evaluate(values) + self.right.evaluate(values)
    
class MultiplicationVariable(Variable):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) * self.right
        return self.left.evaluate(values) * self.right.evaluate(values)
    
class PowerVariable(Variable):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) ** self.right
        return self.left.evaluate(values) ** self.right.evaluate(values)

values = {"x_1": 3, "x_2": -4}

x_1 = Variable(name="x_1")
x_2 = Variable(name="x_2")

a1 = x_1 + x_2 # give us an AdditionVariable!!
print(a1.evaluate(values) == -1)

a2 = a1 + x_1     # z = 2*x_1 + x_2
print(a2.evaluate(values) == 2)

a3 = x_1 + 3    # x_1.__add__(3)
print(a3.evaluate(values) == 6)

a4 = -1 + x_2
print(a4.evaluate(values) == -5)

b1 = x_1 * x_2
print(b1.evaluate(values) == -12)

b2 = x_2 * x_1
print(b2.evaluate(values) == -12)

b3 = b1 * b2
print(b3.evaluate(values) == 144)

b4 = x_1 * 3
print(b4.evaluate(values) == 9)

b5 = 3 * x_1
print(b5.evaluate(values) == 9)

c1 = x_1 ** 2
print(c1.evaluate(values) == 9)

d1 = x_1 - x_2
print(d1.evaluate(values) == 7)

d2 = 2 - x_2
print(d2.evaluate(values) == -6)

e1 = x_1 / x_2
print(e1.evaluate(values) == -0.75)

e2 = x_2 / x_1
print(e1.evaluate(values) == 4 / 3)
print(4/3)

