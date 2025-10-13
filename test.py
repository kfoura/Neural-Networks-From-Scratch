import numpy as np
class neuron:
    def __init__(self, weight: np.array, bias: float):
        self.weight = weight
        self.bias = bias

    def activate(self, input: np.array) -> int:
        return np.dot(self.weight, input) + self.bias


class layer:
    def __init__(self, weights, biases):
        self.neurons = []
        for i in range(len(biases)):
            self.neurons.append(neuron(weights[i], biases[i]))
        
    def activate(self, input):
        output = []
        for i in self.neurons:
            output.append(i.activate(input))
        return output








inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
neurons = layer(weights, biases)
outputs = neurons.activate(inputs)
print(outputs)


