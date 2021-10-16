N = int(input())
A = [[0] * N for i in range(N)]
T = [[0] * N for i in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        T[i][j] = A[j][i]
        print(T[i][j], end = ' ')
    print()