import numpy
import numpy as np

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.input

    def setInput(self, input:list):
        self.input = input

    def activate(self, inputs):
        inputs = numpy.array(inputs)
        return np.dot(inputs, self.weights) + self.bias



class layer:
    def __init__(self, weights: np.array, biases: np.array):
        self.weights = np.array(weights)
        self.biases = np.array(biases)

    def activate(self, inputs):
        return np.dot(inputs, self.weights.T) + biases



inputs = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
neurons = layer(weights, biases)
outputs = neurons.activate(inputs)

weights = [[0.5, 1, -.9], [-.1, .25, .8], [-.70, -1, -.5], [.9, .6, -.3]]
biases = [7, 9, -5, -1]
hidden_layer = layer(weights, biases)
outputs = hidden_layer.activate(outputs)
print(outputs)
