class neuron:

    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def dot_product(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += self.weight * input[i] + self.bias
        return sum