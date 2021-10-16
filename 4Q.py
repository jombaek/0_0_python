def Map(func, l):
    result = []
    for x in l:
        result.append(func(x))
    return result

print(sum(Map(lambda x: x**2, [2, 3])))