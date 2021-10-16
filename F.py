N, M = [int(i) for i in input().split()]
a = []
b = []
min = 100
max = 0

for i in range(N):
    b = [int(j) for j in input().split()]
    for j in range(M):
        int_k = b[j]
        if int_k > max:
            max = int_k
        if int_k < min:
            min = int_k
    a.append(b)

print(a)
print(min, ' ', max)
#a.append([int(j) for j in input().split()])
    

'''for i in range(N):
    for j in range(M):
        if a[i][j] < min:
            min = a[i][j]
        if a[i][j] > max:
            max = a[i][j]'''
            
temp_b = 0

'''for i in range(N):
    for j in range(min, max+1):
        if min <= j <= max:
            temp_b = 0
            for ij in range (M):
                if a[i][ij] == j:
                    temp_b += 1
            print(temp_b, end = ' ')
        else:
            print(0, end = ' ')
    print()'''
