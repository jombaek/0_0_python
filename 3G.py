N = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
new_a = [str(sum(x)) for x in zip(a1, a2)]
print(' '.join(new_a))