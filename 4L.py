#a = list(map(int, input().split())); print(' '.join(map(str, [a[i] ** 2 for i in range(len(a) - 1, -1, -1) if a[i] > 0])))


print(' '.join(map(str, list(reversed([(int(x) ** 2) for x in input().split() if int(x) > 0])))))