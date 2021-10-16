N, M = map(int, input().split())
a = list(map(int, input().split()))
ind = list(map(int, input().split()))

for i in range(M):
    ind[i] -= 1

for j in range(N):
    if j in ind:
        a[j] += 1
    print(a[j], end = ' ')