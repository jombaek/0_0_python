def is_palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

s = input()

result = is_palindrome(s)
print(result)