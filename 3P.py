def rotate_matrix(a):
    return list(list(elem) for elem in zip(*a[::-1]))

n, m, k = map(int, input().split())
k %= 4
result = []

for _ in range(n):
    result.append(input().split())

for _ in range(k):
    result = rotate_matrix(result)

print(*(' '.join(map(str, i)) for i in result), sep='\n')