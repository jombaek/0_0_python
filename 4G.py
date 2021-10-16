from math import sqrt

a = list(map(float, input().split()))
s = 0

for x in a:
    s += x * x

result = sqrt(s)
print(result)