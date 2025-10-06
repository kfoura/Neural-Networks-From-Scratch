import numpy as np


class Neuron():

    def __init__(self, wt, bias):
        self.wt = np.array([bias]+wt)
        # self.bias = bias

    
    def output(self, input):
        return np.dot(self.wt, np.array([1]+input))
    

n = Neuron([1,2,3], 3)


print(n.output([3,7,5]))
print(np.dot(np.array([1,2,3]), np.array([3,7,5]))+3)