with open('input.txt', 'r') as fin:
    A, B  = map(int, fin.read().split())
k = 0
if (A + B) % 2 != 0:
    if A > B:
        k = A + B - 1
    else:
        k = B + A - 1
else:
    k = 0
if k % 4 == 0:
    with open('output.txt', 'w') as fout:
        print(k, file=fout)
else:
    with open('output.txt', 'w') as fout:
        print("0", file=fout)
