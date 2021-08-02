# 이항 계수 1

n,k = map(int,input().split())

# 0<=k<=n 일때 이항계수
# n!/(k!(n-k)!)

summ1=1
summ2=1
summ3=1

# n!
for i in range(1,n+1):
    summ1=summ1*i

# (n-k)!
for i in range(1,n-k+1):
    summ2=summ2*i

# k!
for i in range(1,k+1):
    summ3=summ3*i

print(int(summ1/(summ3*summ2)))