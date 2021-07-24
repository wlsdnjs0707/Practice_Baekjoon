# 영화감독 숌

n = int(input())

i=100
answer =[]

while len(answer)<10000:
    num=list(str(i))
    for j in range(len(num)-1,0,-1):
        if j>=2:
            if num[j]=='6' and num[j-1]=='6' and num[j-2]=='6':
                answer.append(num)

    i+=1

print(''.join(answer[n-1]))