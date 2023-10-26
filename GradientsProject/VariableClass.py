import math
import numpy as np
import torch

from typing import Any

# QUESTIONS:

# how do i handle taking the gradient of ints and stuff like that?
# no handlers

class Variable: # for the independent variables
    def __init__(self, name=None):
        self.name = name

    # The evaluation method for independent variables, base case
    def evaluate(self, values): 
        # values will be a dictionary that looks like: {"x_0": 3, "x_1": -4}
        return values[self.name]
    
    def grad(self, values):
        arr = np.zeros(len(values))
        str_index = self.name[2:]
        int_index = int(str_index)
        arr[int_index] = 1
        return arr
        
    # NON-OPERATIONAL MAGIC METHODS

    # Variables now have callable instances
    def __call__(self, values):
        return self.evaluate(values)

    # Print funcitons
    def __repr__(self, values):
        return self.evaluate(values)

    # OPERATIONAL MAGIC METHODS
    
    def __add__(self, other):
        return AdditionVariable(self, other)
    
    def __radd__(self, other):
        return AdditionVariable(self, other)
    
    def __sub__(self, other):
        # references the __add__ magic method so that I don't have to do extra work lol
        return self + other * (-1)
    
    def __rsub__(self, other):
        return  self * (-1) + other

    def __mul__(self, other):
        return MultiplicationVariable(self, other)
    
    def __rmul__(self, other):
        return MultiplicationVariable(self, other)
    
    def __pow__(self, other):
        return PowerVariable(self, other)
    
    def __rpow__(self, other):
        return PowerVariable(other, self)
    
    def __truediv__(self, other):
        return self * (other ** -1)
    
    def __rtruediv__(self, other):
        return (other ** -1) * self

    # both these static methods use other because it's static so self doesn't exist

    @staticmethod
    def exp(other):
        return ExpVariable(other)

    @staticmethod
    def log(other):
        return LogVariable(other)

class LogVariable(Variable):
    def __init__(self, arg):
        self.arg = arg

    def evaluate(self, values):
        return math.log(self.arg.evaluate(values))
    
    def grad(self, values):
        return self.arg.grad(values) / self.arg.evaluate(values)

class ExpVariable(Variable):
    def __init__(self, exp):
        self.exp = exp
    
    def evaluate(self, values):
        if isinstance(self.exp, (int, float)):
            return math.e ** self.exp
        return math.e ** self.exp.evaluate(values)
    
    # bad
    def grad(self, values):
        return self.exp.grad(values) * math.e ** self.exp.evaluate(values)
    
class AdditionVariable(Variable):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # override the evaluate method (recursive step)
    def evaluate(self, values):
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) + self.right
        return self.left.evaluate(values) + self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.right, (float, int)):
            return self.left.grad(values)
        if isinstance(self.left, (float, int)):
            return self.right.grad(values)
        return self.left.grad(values) + self.right.grad(values)
    
class MultiplicationVariable(Variable):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) * self.right
        return self.left.evaluate(values) * self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.right, (float,int)):
            return self.left.grad(values) * self.right
        if isinstance(self.left, (float,int)):
            return self.right.grad(values) * self.left
        return self.left.evaluate(values) * self.right.grad(values) + self.left.grad(values) * self.right.evaluate(values)
    
class PowerVariable(Variable):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.right, (int, float)) and isinstance(self.left, (int, float)):
            return self.left ** self.right
        if isinstance(self.left, (int, float)):
            return self.left ** self.right.evaluate(values)
        if isinstance(self.right, (int, float)):
            return self.left.evaluate(values) ** self.right
        return self.left.evaluate(values) ** self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.right, (float, int)):
            return self.right * (self.left.evaluate(values) ** (self.right - 1)) * self.left.grad(values)
        return self.right.evaluate(values) * (self.left.evaluate(values) ** (self.right.evaluate(values) - 1)) * self.left.grad(values)

# build LogVar and ExpVar tests
def var_tests():
    values = {"x_0": 3, "x_1": -4}

    x_0 = Variable(name="x_0")
    x_1 = Variable(name="x_1")

    print(x_0(values))

    a1 = x_0 + x_1 # give us an AdditionVariable!!
    assert (a1(values) == -1), f'a1() == -1 failed, {a1(values)}'

    a2 = a1 + x_0 # z = 2*x_0 + x_1
    assert (a2(values) == 2), f'a2() == 2 failed, {a2(values)}'

    a3 = x_0 + 3    # x_0.__add__(3)
    assert (a3(values) == 6), f'a2() == 2 failed, {a3(values)}'

    a4 = -1 + x_1
    assert (a4(values) == -5), f'a4() == -5 failed, {a4(values)}'

    b1 = x_0 * x_1
    assert (b1(values) == -12), f'b1() == -12 failed, {b1(values)}'

    b2 = x_1 * x_0
    assert (b2(values) == -12), f'b2() == -12 failed, {b2(values)}'

    b3 = b1 * b2
    assert (b3(values) == 144), f'b3() == 144 failed, {b3(values)}'

    b4 = x_0 * 3
    assert (b4(values) == 9), f'b4() == 9 failed, {b4(values)}'

    b5 = 3 * x_0
    assert (b5(values) == 9), f'b5() == 9 failed, {b5(values)}'

    c1 = x_0 ** 2
    assert (c1(values) == 9), f'c1() == 9 failed, {c1(values)}'

    d1 = x_0 - x_1
    assert (d1(values) == 7), f'd1() == 7 failed, {d1(values)}'

    d2 = 2 - x_1
    assert (d2(values) == 6), f'd2() == 6 failed, {d2(values)}'

    d3 = 2 - x_0
    assert (d3(values) == -1), f'd3() == -1 failed, {d3(values)}'

    d4 = x_0 - 2
    assert (d4(values) == 1), f'd4() == 1 failed, {d4(values)}'

    e1 = x_0 / x_1
    assert (e1(values) == -0.75), f'e1() == -0.75 failed, {e1(values)}'

var_tests()

def grad_tests():

    # Clean Test Code

    values = {"x_0": 3, "x_1": 1, "x_2": 7}

    x_0 = Variable(name = "x_0")
    x_1 = Variable(name = "x_1")
    x_2 = Variable(name = "x_2")

    z = Variable.exp(x_0 + x_1**2) + 3 * Variable.log(27 - (x_0 * x_1 * x_2))

    x_0t = torch.tensor(3., requires_grad=True)
    x_1t = torch.tensor(1., requires_grad=True)
    x_2t = torch.tensor(7., requires_grad=True)

    zt = torch.exp(x_0t + x_1t**2) + 3 * torch.log(27 - x_0t * x_1t * x_2t)
    zt.backward()

    assert (z.grad(values)[0] >= x_0t.grad - 0.1 and z.grad(values)[0] <= x_0t.grad + 0.1), f'z.grad[0] failed, {z.grad[0]}'
    assert (z.grad(values)[1] >= x_1t.grad - 0.1 and z.grad(values)[1] <= x_1t.grad + 0.1), f'z.grad[1] failed, {z.grad[1]}'
    assert (z.grad(values)[2] >= x_2t.grad - 0.1 and z.grad(values)[2] <= x_2t.grad + 0.1), f'z.grad[1] failed, {z.grad[2]}'

    values = {"x_0": 2, "x_1": 4, "x_2": 5}

    x_0t = torch.tensor(2., requires_grad=True)
    x_1t = torch.tensor(4., requires_grad=True)
    x_2t = torch.tensor(5., requires_grad=True)

    c = Variable.exp(x_0 + x_1**2)

    ct = torch.exp(x_0t + x_1t**2)
    ct.backward()

    assert (c.grad(values)[0] >= x_0t.grad - 0.1 and c.grad(values)[0] <= x_0t.grad + 0.1), f'c.grad[0] failed, {c.grad[0]}'
    assert (c.grad(values)[1] >= x_1t.grad - 0.1 and c.grad(values)[1] <= x_1t.grad + 0.1), f'c.grad[1] failed, {c.grad[1]}'
    #assert (c.grad(values)[2] >= x_2t.grad - 0.1 and c.grad(values)[2] <= x_2t.grad + 0.1), f'c.grad[2] failed, {c.grad[2]}'

grad_tests()