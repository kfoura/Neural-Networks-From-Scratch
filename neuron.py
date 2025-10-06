import numpy as np;

class point:
    
    def __init__ (self, weight, bias):
        self.weight = weight;
        self.bias = bias;

    def dot(self, input):
        return np.dot(input, weight);
        