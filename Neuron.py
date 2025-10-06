class Neuron:

    def __init__(self):
        self.weights = [0,0,0,0,0]
        self.bias = 0.0
        self.input = [0,0,0,0,0]
    
    def __init__(self, weights:list, bias:float):
        self.weights = weights
        self.bias = bias
        self.input

    def setInput(self, input:list):
        self.input = input
    
    def activate(self):
        output = 0
        for i in range (self.weights):
            output += self.weights[i] * self.input[i]
        output += self.bias
        return output
        
    

