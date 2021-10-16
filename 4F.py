a = list(map(int, input().split()))
s = 0

for x in a:
    s += abs(x)
print(s)