import numpy as np
class neuron:
    def __init__(self, weight: np.array, bias: float):
        self.weight = weight
        self.bias = bias
    
    def activate(self, input: np.array) -> int:
        return np.dot(self.weight, input) + self.bias

