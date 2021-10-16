with open('input.txt', 'r') as fin:
    H1, M1, H2, M2  = map(int, fin.read().split())
if M1 + M2 < 60:
    M = M1 + M2
    h = 0
else:
    M = M1 + M2 - 60
    h = 1
if H1 + H2 + h < 24:
    H = H1 + H2 + h
else:
    H = H1 + H2 + h - 24 * ((H1 + H2 + h) // 24)
with open('output.txt', 'w') as fout:
    print(H, M, file=fout)
