def Join(array, separator=' '):
    s = str(array[0])
    for i in range(1, len(array)):
        s += separator + array[i]
    return s

ary = ['aa', 'bb', 'cc']
print(Join(ary))