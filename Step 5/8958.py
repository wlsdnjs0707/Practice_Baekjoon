# OX퀴즈

t = int(input())

for i in range(t):
    ox_list = list(input())

    score = 0
    bonus = 0

    for i in range(len(ox_list)):
        if ox_list[i] == 'O':
            bonus += 1
        elif ox_list[i] == 'X':
            bonus = 0
        score = score + bonus

    print(score)