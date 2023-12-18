import numpy as np

from gradx import xopl


def test_simple():
    op = xopl()
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    added = op.add(a, b)
    multiplied = op.mul(a, b)

    assert added.shape == a.shape
    print("Addition Test passed")
    assert multiplied.shape == (a.shape[0], b.shape[1])
    print("Multiplication Test passed")
