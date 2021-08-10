# 수 찾기

n = int(input())

seq = list(map(int,input().split()))

m = int(input())

seq2 = list(map(int,input().split()))

seq.sort()

def binary(array,target,start,end):
    if start>end:
        return None
    
    mid = (start+end)//2

    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary(array,target,start,mid-1)
    else:
        return binary(array,target,mid+1,end)

for i in range(len(seq2)):
    result=binary(seq,seq2[i],0,len(seq2)-1)
    if result==None:
        print(0)
    else:
        print(1)