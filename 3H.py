a = list(map(int, input().split()))
h = []
k = 0
for x in a:
    if x in h:
        continue
    else:
        h.append(x)
        k += 1
print(k)