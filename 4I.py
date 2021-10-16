p = int(input())
v = list(map(int, input().split()))
n, m = map(int, input().split())

A = [[0] * m for i in range(n)]
ind = 0

for i in range(n):
    for j in range(m):
        A[i][j] = v[ind]
        ind += 1
        if j == m - 1:
            print(A[i][j], end = '')
        else:
            print(A[i][j], end = ' ')
    print()