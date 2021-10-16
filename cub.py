from math import *
import time

N = 3
d = [0] * (N + 5)

memory = { '0' : None }

def print_debug(turns, wins):
    print('turns = ' + str(turns) + ' wins = ' + str(wins))

def print_result(turns, wins):
    # print(str(turns) + ' ' + str(wins))
    print(round(turns / wins, 5))

def manual_input():
    N = int(input())
    d = [0] * (N + 5)
    S = input().split()
    for i in range(len(S)):
        d[i] = int(S[i])

def turn(start, i):
    if d[i] == 0:
        return start + i
    return d[d[i]]

def play(combination):
    position = 1
    for i, num in enumerate(combination):
        position = turn(position, int(num))
        if position >= N:
            return i + 1
    return 0    

def increment_combination(s):
    last = int(s[-1]) + 1
    if last <= 6:
        return s[:-1] + str(last)
    elif len(s) == 1:
        return '11'
    else:
        return increment_combination(s[:-1]) + '1'

def transfer(combination):
    new_s = ''
    for i in combination:
        new_s += str(int(i)-1)
    return new_s

# def generate_combinations(num_of_dice):
#     s = '1'
#     while len(s) <= num_of_dice:
#         yield s
#         s = increment_combination(s)

def turns_for_win(combination):
    turns = 0
    new_combination = '' + combination[turns]
    while turns < len(combination):
        if new_combination in memory:
            return turns + 1
        new_combination += combination[turns]
        turns += 1
    return 0

def skip(combination, add_turns):
    new_combination = increment_combination(combination[:-1] + '6')
    if (combination[add_turns] == '6'):
        return (increment_combination(combination[:add_turns]) + combination[add_turns + 1:], int(transfer(new_combination), 6) - int(transfer(combination), 6))
    new_combination = increment_combination(combination[:-1] + '6')
    num_of_skips = int(transfer(new_combination), 6) - int(transfer(combination), 6)
    return (new_combination, num_of_skips)

def solution(precision = 8):
    combination = '1'
    turns = 0
    wins = 0
    while len(combination) <= precision:
        #print(combination, end=' ')
        result = play(combination)
        if result > 0:
            wins += 1
        turns += result
        combination = increment_combination(combination)
        #print_debug(turns, wins)
    print_result(turns, wins)

def solution_optimized(precision = 8):
    combination = '1'
    turns = 0
    wins = 0
    while len(combination) <= precision:
        #print(combination, end=' ')
        add_turns = turns_for_win(combination)
        if add_turns == 0:
            result = play(combination)
            if result > 0:
                memory[combination] = 1
                wins += 1
                turns += result
                #print_debug(turns, wins)
                combination, skips = skip(combination, add_turns)
                turns += result * skips
                wins += skips
                continue
            #print_debug(turns, wins)
            combination = increment_combination(combination)
        else:
            turns += add_turns
            wins += 1
            #print_debug(turns, wins)
            combination, skips = skip(combination, add_turns)
            turns += add_turns * skips
            wins += skips
    print_result(turns, wins)

start = time.time()
solution(4)
end = time.time()
print("Elapsed time for solution: " + str(end - start))

start = time.time()
solution_optimized(4)
end = time.time()
print("Elapsed time for optimized solution: " + str(end - start))
