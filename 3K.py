def output(list):
    s = str(list[0])
    for x in list[1:]:
        s += ', ' + str(x)
    return s

import sys
a = [line.strip() for line in sys.stdin.readlines()]

a1, a2 = [], []
for i, x in enumerate(a):
    if i % 2 == 0:
        a1.append(x)
    else:
        a2.append(x)
print(output(a1))
print(output(a2))
