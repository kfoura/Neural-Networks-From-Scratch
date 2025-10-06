import numpy
import numpy as np

def __init__(self, weights, bias):
    self.weights = weights
    self.bias = bias

def activate(self, inputs):
    inputs = numpy.array(inputs)
    return np.dot(inputs, self.weights) + self.bias

