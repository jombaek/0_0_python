import string

s = input()

for x in s:
    if x in string.punctuation:
        s = s.replace(x, "")

result = len(s.split())

print(result)