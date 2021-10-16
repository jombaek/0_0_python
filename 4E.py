s = input()
position = int(input())

s = s.split()

if position <= len(s):
    print(s[position - 1])
else:
    print(s[-1])