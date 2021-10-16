N = int(input())
a = [input() for i in range(N)]
k = 0
for x in a:
    if x.lower() == 'boletus edulis':
        k += 1
print(k)