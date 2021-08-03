# 오큰수

n = int(input())

seq=list(map(int,input().split()))

temp=[]
nge=[]

for i in range(n):
    for j in range(i,n):
        if seq[i]<seq[j]:
            temp.append(seq[j])
    
    if len(temp)!=0:
        nge.append(temp[0])
    elif len(temp)==0:
        nge.append(-1)
    temp.clear()

for i in nge:
    print(i,end=' ')