def shift(list, steps):
    for i in range(steps):
        list.append(list.pop(0))
    return list

def output(list):
    for x in list:
        print(x, end = ' ')

N, K = map(int, input().split())
a = list(map(int, input().split()))
output(shift(a, K))