from copy import copy
import sys
import copy

a_lst = [[int(ch) for ch in row] for row in sys.stdin.read().replace('.', '0').replace('#', '1').split()]

# with open('input.txt', 'r') as fin:
#     a_lst = [[int(ch) for ch in row] for row in fin.read().replace('.', '1').replace('#', '0').split()]

m = len(a_lst)
n = len(a_lst[0]) if m else 0
b_lst = copy.deepcopy(a_lst)

def neighborsCount(vec, a_lst):
    neighbors = [[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]
    count = 0
    for i in neighbors:
        if a_lst[(vec[0] + i[0]) % len(a_lst)][(vec[1] + i[1]) % len(a_lst[0])] == 0:
            count += 1
    return count

def gameOfLife(a_lst, b_lst, n, m):
    for i in range(m):
        for j in range(n):
            if a_lst[i][j] == 0:
                lives = neighborsCount([i, j], a_lst)
                if lives < 2 or lives > 3:
                    b_lst[i][j] = '.'
                else:
                    b_lst[i][j] = '#'
            else:
                lives = neighborsCount([i, j], a_lst)
                if lives == 3:
                    b_lst[i][j] = '#'   
                else:
                    b_lst[i][j] = '.'
    return b_lst

result = gameOfLife(a_lst, b_lst, n, m)

print(*(''.join(map(str, i)) for i in result), sep='\n')