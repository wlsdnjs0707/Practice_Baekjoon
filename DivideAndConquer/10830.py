# 행렬 제곱

n,b = map(int,input().split())

seq=[]

for i in range(n):
    seq.append(list(map(int,input().split())))

def multiple(n,a,b):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=a[i][k]*b[k][j]
            result[i][j]%=1000

    return result

def divide(n,x,a):
    if x==1:
        return a
    elif x==2:
        return multiple(n,a,a)
    else:
        temp=divide(n,x//2,a)
        if x%2==0:
            return multiple(n,temp,temp)
        else:
            return multiple(n,multiple(n,temp,temp),a)
            
result=divide(n,b,seq)

for row in result:
    for num in row:
        print(num%1000,end=' ')
    print()

