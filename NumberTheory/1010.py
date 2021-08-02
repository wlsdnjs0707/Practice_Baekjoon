# 다리 놓기

t = int(input())

for _ in range(t):
    n,m=map(int,input().split())

    # 오른쪽 m개중 n개를 뽑는다(중복없이)
    # mCn = m!/n!(m-n)!

    summ1=1
    summ2=1
    summ3=1

    for i in range(1,m+1):
        summ1=summ1*i
    
    for i in range(1,n+1):
        summ2=summ2*i
    
    for i in range(1,m-n+1):
        summ3=summ3*i
    
    print(int(summ1/(summ2*summ3)))

