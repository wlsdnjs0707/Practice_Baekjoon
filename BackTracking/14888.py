# 연산자 끼워넣기

n = int(input())

numbers = list(map(int,input().split()))

# 덧셈,뺄셈,곱셈,나눗셈의 개수
operators = list(map(int,input().split()))

copy=[]
for i in range(4):
    copy.append(operators[i])

q = []

def dfs(x,summ):

    if x==len(numbers)-1:
        q.append(summ)
        return

    if operators[0]>=1:
        summ = summ + numbers[x+1]
        operators[0]-=1
        dfs(x+1,summ)
        operators[0]+=1
        summ = summ - numbers[x+1]

    if operators[1]>=1:
        summ = summ - numbers[x+1]
        operators[1]-=1
        dfs(x+1,summ)
        operators[1]+=1
        summ = summ + numbers[x+1]

    if operators[2]>=1:
        summ = summ * numbers[x+1]
        operators[2]-=1
        dfs(x+1,summ)
        operators[2]+=1
        summ = summ // numbers[x+1]

    if operators[3]>=1:
        if summ<0:
            summ=-1*summ
            summ=summ//numbers[x+1]
            summ=-1*summ
        else:
            summ = summ // numbers[x+1]
        operators[3]-=1
        dfs(x+1,summ)
        operators[3]+=1
        summ = summ * numbers[x+1]

    return

dfs(0,numbers[0])
print(max(q))
print(min(q))