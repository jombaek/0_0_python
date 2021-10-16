a = list(map(int, input().split()))

min = a[0]
max = a[0]

for x in a:
    if x > max:
        max = x
    if x < min:
        min = x

for x in a:
    if x == max:
        x = min
    print(x, end = ' ')