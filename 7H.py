import numpy as np

def weighted_moving_average(y, w):
    return np.convolve(y, w[::-1], mode ='valid') / np.sum(w)

with open('input.txt', 'r') as fin:
    n, m = [int(x) for x in fin.readline().split()]
    w = np.array([float(x) for x in fin.readline().split()])
    y = np.array([float(x) for x in fin.readline().split()])

with open('output.txt', 'w') as fout:
    fout.write(' '.join(str(x) for x in weighted_moving_average(y, m, w)))