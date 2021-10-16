def output(list):
    s = str(list[0])
    for x in list[1:]:
        s += ' ' + str(x)
    return s

with open('input.txt', 'r') as fin:
    N = fin.readline()
    a = list(map(int, fin.read().split()))

result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(result)):
    for x in a:
        if i == x:
            result[i] += 1

result.append(result.pop(0))

with open('output.txt', 'w') as fout:
    print(output(result), file=fout)
