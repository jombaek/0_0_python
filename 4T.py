with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    a = []
    for i in range(n - 1):
        a.append((fin.readline()[:-1].split('\t')))
    a.append((fin.readline().split('\t')))

d = {}

for key, value in a:
    if key not in d:
        d[key] = []
    d[key].append(value)

d = dict(sorted(d.items()))

wrote_first_key = False
with open('output.txt', 'w') as fout:
    for key in d.keys():
        if not wrote_first_key:
            fout.write(key)
            wrote_first_key = True
        else:
            fout.write('\n' + key)
        d[key] = sorted(d[key])
        for value in d[key]:
            fout.write('\n' + value)