# K번째 수

n = int(input())
k = int(input())

a=[]

# for i in range(n):
#     for j in range(n):
#         a.append((i+1)*(j+1))

# a.sort()
# print(a[k])

start=1
end=k
answer=0

while start<=end:
    mid = (start+end)//2

    temp=0

    for i in range(1,n+1):
        temp+=min(mid//i,n)
    
    if temp>=k:
        answer=mid
        end=mid-1
    else:
        start=mid+1

print(answer)