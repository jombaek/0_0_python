import numpy as np

def moving_average(a, m):
    return np.convolve(a, np.ones(m), 'valid') / m

with open('input.txt', 'r') as fin:
    n, m = [int(x) for x in fin.readline().split()]
    a = np.array([float(x) for x in fin.readline().split()])

with open('output.txt', 'w') as fout:
    fout.write(' '.join(str(x) for x in moving_average(a, m)))