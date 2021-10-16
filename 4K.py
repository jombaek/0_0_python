a = list(map(str, input().split()))

sorted_a = sorted(a, key = lambda x: x[1])

for x in sorted_a[:-1]:
    print(x, end = ' ')
print(sorted_a[-1])