import numpy as np
N = int(input())
a = [int(i) for i in input().split()]
b = []
s = 0
for i in range(len(a)):
    for k in range(N):
        s += np.exp(a[k])
    b.append(np.exp(a[i])/s)
    s = 0
for i in b:
    print(i, end = ' ')
