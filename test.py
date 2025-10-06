import numpy as np

inputs = np.array([1, 2, 3])


class Neuron:
    def __init__(self, weights: np.ndarray, bias: float):
        self.weights = weights
        self.bias = bias

    def dot(self, inputs: np.ndarray) -> float:
        return float(np.dot(inputs, self.weights) + self.bias)
