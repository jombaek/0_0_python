a = list(map(int, input().split()))
print(' '.join(map(str, a[:2] + list(reversed(a[2:-2])) + a[-2:])))

