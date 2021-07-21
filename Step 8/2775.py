# 부녀회장이 될테야

t = int(input()) # Test Case

for e in range(t):
    k = int(input()) # 0층 ~ k층
    n = int(input()) # 1호 ~ n호

    count=0
    apartment=[]

    for i in range(k+1):
        apartment.append([0]*n)

    for j in range(len(apartment[0])):
        apartment[0][j]=j+1

    for i in range(k+1):
        apartment[i][0]=1

    for i in range(1,k+1):
        for j in range(1,n):
            apartment[i][j]=apartment[i-1][j]+apartment[i][j-1]

    print(apartment[k][n-1])