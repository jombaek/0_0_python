def gcd(m, n):
    while m != 0 and n != 0:
        if m > n:
            m %= n
        else:
            n %= m
    return m + n

A, B, C = map(int, input().split())

print(gcd(A, B), gcd(A, C), gcd(B, C))