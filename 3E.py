def to_snake_case(s):
    new_s = s[0].lower()
    for x in s[1:]:
        if x.isupper():
            new_s += '_' + x.lower()
        else:
            new_s += x
    return new_s

def to_camel_case(s):
    new_s = s[0].upper()
    to_upper = False
    for x in s[1:]:
        if x != '_':
            if to_upper:
                new_s += x.upper()
                to_upper = False
            else:
                new_s += x
        else:
            to_upper = True
    return new_s

with open('input.txt', 'r') as fin:
    s  = fin.read()

result = ''
if s:
    if s == s.lower():
        result = to_camel_case(s)
    else:
        result = to_snake_case(s)
        
with open('output.txt', 'w') as fout:    
    fout.write(result)