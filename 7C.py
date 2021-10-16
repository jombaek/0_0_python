import numpy as np

def WAM(a):
    return round(np.average(a.T[0], weights = a.T[1]), 3)

def WHM(a):
    return round(np.sum(a.T[1] / np.sum(a.T[1] / a.T[0])), 3)

def WGM(a):
    return round(np.exp((1 / np.sum(a.T[1])) * np.sum(a.T[1] * np.log(a.T[0]))), 3)

with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    a = np.array([float(x) for x in fin.read().split()])

b = a.reshape(n, 2)

result = str(WAM(b)) + ' ' + str(WHM(b)) + ' ' + str(WGM(b))

with open('output.txt', 'w') as fout:
    fout.write(result)