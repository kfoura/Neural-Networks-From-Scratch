import numpy as np
import nnfs
from nnfs.datasets import spiral_data
import matplotlib.pyplot as plt

nnfs.init()

class Nueron:
    def __init__(self, weights: np.array, bias: float):
        self.weights = weights
        self.bias = bias

    def output(self, inputs) -> int:
        return np.dot(self.weights, inputs) + self.bias
    

class Layer_Dense:
    def __init__(self, n_inputs, n_nuerons):
        self.weights = 0.01 * np.random.randn(n_nuerons, n_inputs)
        self.biases = np.zeros((1, n_nuerons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights.T) + self.biases


class activate_ReLU():
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class activate_Softmax:
    def forward(self, inputs):
        exp_vals = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        norm_base = np.sum(exp_vals, axis=1, keepdims=True)
        probabilities = exp_vals / norm_base
        self.output = probabilities


X, y = spiral_data(samples=100, classes=3)
layer1 = Layer_Dense(2, 3)
activation1 = activate_ReLU()
layer1.forward(X)
activation1.forward(layer1.output)
#print(activation1.output[:5])
activation2 = activate_Softmax()
activation2.forward(activation1.output)
print(activation2.output[:5])
