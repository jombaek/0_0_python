def rotate_matrix(m, k):
    T = [[0] * len(m[i]) for i in range(len(m))]
    c = 0
    if k < 0:
        while c != abs(k):
            T = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1, -1, -1)]
            c += 1
            m = T
    else:
        while c != k:
            T = [[m[j][i] for j in range(len(m[0])-1, -1, -1)] for i in range(len(m))]
            c += 1
            m = T
    return m

n, m, k = map(int, input().split())

A = [[0] * m for i in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))

print(rotate_matrix(A, k))