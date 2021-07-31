# 정수 삼각형

n = int(input())
triangle=[]

for i in range(n):
    triangle.append(list(map(int,input().split())))

def dp(level):
    if level==n:
        return

    for i in range(len(triangle[level])):
        if i==0:
            triangle[level][i]+=triangle[level-1][i]
        elif i==len(triangle[level])-1:
            triangle[level][i]+=triangle[level-1][i-1]
        else:
            triangle[level][i]+=max(triangle[level-1][i-1],triangle[level-1][i])

    dp(level+1)

    return

dp(1)

print(max(triangle[n-1]))