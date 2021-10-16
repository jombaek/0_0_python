with open('id.txt', 'r') as fin:
    a = list(map(int, fin.read().split()))

with open('id2.txt', 'r') as fin:
    b = list(map(int, fin.read().split()))

[print(i) for i in a]