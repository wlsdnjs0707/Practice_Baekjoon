# 회의실 배정

n = int(input())

schedule=[]

for i in range(n):
    s,e = map(int,input().split())
    schedule.append([s,e])

sorted_schedule = sorted(schedule,key=lambda x:x[1])

index=0
answer=[sorted_schedule[0]]

for j in range(1,n):
    if sorted_schedule[j][0]>=sorted_schedule[index][1]:
        index=j
        answer.append(sorted_schedule[j])

# print(answer)
print(len(answer))