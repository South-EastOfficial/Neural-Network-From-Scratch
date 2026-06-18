import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        
    def feedforward(self, inputs):
        # Weight inputs, add bias, then use the activation function
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)
    
weights = np.array([0, 1])
bias = 4

n = Neuron(weights, bias)
x = np.array([2, 3])
print(n.feedforward(x))  # Output should be close to 1 since 0*2 + 1*3 + 4 = 7, and sigmoid(7) is close to 1
