l = list(map(int, input().split()))

n = len(l)
i = 0

while i < n - 1:
    if l[i + 1] == 0:
        del l[i]
        n -= 1
        continue
    i += 1

for x in l:
    print(x, end = ' ')