# 문자열 반복

T = int(input())

for i in range(T):
    list_input = list(input().split())
    repeat = int(list_input[0])
    string = list(list_input[1])
    
    list_output = []

    for j in string:
        list_output.append(j*repeat)

    print(''.join(list_output))