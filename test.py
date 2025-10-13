import numpy as np
class neuron:
    def __init__(self, weight: np.array, bias: float):
        self.weight = weight
        self.bias = bias

    def activate(self, input: np.array) -> int:
        return np.dot(self.weight, input) + self.bias


class layer:
    def __init__(self, weights: np.array, biases: np.array):
        self.weights = np.array(weights)
        self.biases = np.array(biases)
        
    def activate(self, inputs):
        return np.dot(inputs, self.weights.T) + self.biases








inputs = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
neurons = layer(weights, biases)
outputs = neurons.activate(inputs)
print(outputs)