N, k, d = [int(i) for i in input().split()]
a = []
for i in range(N):
    a.append([int(j) for j in input().split()])

for i in range(N):
    max = a[i][0]
    min = a[i][0]
    for j in range(k):
        if a[i][j] > max:
            max = a[i][j]
        if a[i][j] < min:
            min = a[i][j]
    if (max - min) <= 2:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
