from VariableClass import *

class LogisticRegressionClass:
    def __init__(self, m=np.random.random(), b=np.random.random()):
        self.m = m
        self.b = b

        x_1 = Variable(name="x_1")
        x_2 = Variable(name="x_2")