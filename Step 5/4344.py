# 평균은 넘겠지

c = int(input())

for i in range(c):

    grade = list(map(int,input().split()))

    summ = 0

    for i in range(grade[0]+1):
        summ = summ + grade[i]

    summ = summ - grade[0]
    summ = summ/grade[0]

    count = 0

    for i in range(grade[0]+1):
        if i==0:
            continue
        else:
            if grade[i]>summ:
                count+=1

    print("{:.3f}%".format(round((count/grade[0])*100,3)))