N = int(input())
a = [int(input()) for i in range(N)]

s = 0

for x in a:
    if s < 1000:
        s += x
    else:
        break
print(s)