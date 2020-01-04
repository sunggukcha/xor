import torch
import torch.nn as nn

class XOR(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        x = input.clone()
        x[ x < 0 ] = 0
        x[ x > 1.6 ] = 0
        return x

    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        grad_input = grad_output.clone()
        grad_input[input < 0] = 0
        grad_input[input > 1.6 ] = 0
        return grad_input
        

class Perceptron(nn.Module):
    def __init__(self, mode='relu'):
        super(Perceptron, self).__init__()
        
        self.neuron = nn.Linear(2, 1)
        self.neuron.weight.data.fill_(1)
        if mode == 'relu':
            print("ReLU activation function")
            self.relu = nn.ReLU()
        elif mode == 'xor':
            print("XOR activation function")
            xor = XOR()
            self.relu = xor.apply
        else:
            raise NotImplementedError


    def forward(self, x):
        x = self.neuron(x)
        x = self.relu(x)
        return x
    
