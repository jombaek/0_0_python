def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

A, B, C = map(int, input().split())

print(gcd(A, B), gcd(A, C), gcd(B, C))