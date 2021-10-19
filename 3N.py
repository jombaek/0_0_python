with open('input.txt', 'r') as fin:
    N = int(fin.readline())
    a = list(map(str, fin.read().split()))

b = []
d = {}

for i in range(len(a)):
    if a[i].lower() not in d:
        b.append(a[i])
        d[a[i].lower()] = 1
    else:
        last_digit = d[a[i].lower()]
        d[a[i].lower()] += 1
        while a[i].lower() + str(last_digit) in d:
            last_digit += 1
        a[i] = a[i] + str(last_digit)
        d[a[i].lower()] = 1
        b.append(a[i])

with open('output.txt', 'w') as fout:
    fout.write('\n'.join(b))