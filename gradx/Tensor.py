import numpy as np


class Xopl:
    def __init__(self):
        pass

    def add(self, matrix_a, matrix_b):
        return np.add(matrix_a, matrix_b)

    def mul(self, matrix_a, matrix_b):
        return np.dot(matrix_a, matrix_b)
