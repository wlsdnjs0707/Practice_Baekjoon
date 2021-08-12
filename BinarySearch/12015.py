# 가장 긴 증가하는 부분 수열 2
# LIS

def binary(target,array):
    start = 0
    end = len(array)-1
    mid=(start+end)//2

    while end-target>=0:
        if target==array[mid]:
            return mid
        elif target>=array[mid]:
            start=mid+1
        elif target<array[mid]:
            end=mid-1
        mid=(start+end)//2

    return -1

n = int(input())
seq = list(map(int,input().split()))
lis = []

for i in range(len(seq)):

    if len(lis)==0:
        lis.append(seq[i])

    s=0
    e=len(lis)-1

    while s<=e:
        mid=(s+e)//2
        if lis[mid]<seq[i]:
            s=mid+1
        else:
            e=mid-1
    
    if s>=len(lis):
        lis.append(seq[i])
    else:
        lis[e]=seq[i]

print(len(lis))