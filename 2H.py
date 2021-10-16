from math import *

D, T = float(input()), float(input())
v1, v2 = float(input()), float(input())
w1, w2 = float(input()), float(input())

if (v1 - w1) == 0:
    t1 = 0
else:
    t1 = (D - w1 * T) / (v1 - w1)
    if t1 > T:
        t1 = 0

if (v1 - w2) == 0:
    t2 = 0
else:
    t2 = (D - w2 * T) / (v1 - w2)
    if t2 > T:
        t2 = 0
        
if (v2 - w1) == 0:
    t3 = 0
else:
    t3 = (D - w1 * T) / (v2 - w1)
    if t3 > T:
        t3 = 0

if (v2 - w2) == 0:
    t4 = 0
else:
    t4 = (D - w2 * T) / (v2 - w2)
    if t4 > T:
        t4 = 0

print(round(abs(max((v1 * t1), (v1 * t2), (v2 * t3), (v2 * t4))), 3))
