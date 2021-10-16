def find_wall(x, A, B):
    if x < A:
        return 'S'
    else:
        x -= A
    if x < B:
        return 'E'
    else:
        x -= B
    if x < A:
        return 'N'
    else:
        x -= A
    if x < B:
        return 'W'
    else:
        x -= B

with open('input.txt', 'r') as fin:
    A, B, t = map(int, fin.read().split())
x = t % (2*A + 2*B)
with open('output.txt', 'w') as fout:
    print(find_wall(x, A, B), file=fout)


