import numpy as np

class Perceptron():
    weights: list
    value: float
    active: bool

    def __init__(self, inputs_number: int):
        if inputs_number < 1:
            raise Exception('Invalid number of inputs')
        self.weights = np.ones(inputs_number) * 0.5
        self.value = None
        self.active = None

    def feed(self, values: np.array):
        self.value = np.dot(self.weights, values)
        return self

    def activate(self):
        if self.value > 0.5:
            self.active = True
        else:
            self.active = False
        return self

    def __str__(self):
        return(f'Weights: {self.weights}. Value: {self.value}. Active: {self.active}')
