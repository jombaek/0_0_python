with open('d.in', 'r') as fin:
    s  = fin.read()

for punc in ['.', ',', '!', '?', ' -', '- ']:
    s = s.replace(punc, ' ')

result = len(s.split())

with open('d.out', 'w') as fout:    
    fout.write(str(result))
