a = list(map(int, input().split()))

min = min(a)
max = max(a)

for i in range(len(a)):
    if a[i] == max:
        a[i] = min
    print(a[i], end = ' ')