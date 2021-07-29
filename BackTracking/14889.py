# 스타트와 링크

n = int(input())

score=[]

for i in range(n):
    score.append(list(map(int,input().split())))

# n명이 2팀, 각 팀당 n/2명

visited=[0]*n
p = []
q = []
temp1=[]
temp2=[]
answer=[]

def dfs(x):

    if x==n/2:
        for i in range(n):
            if i+1 not in q:
                p.append(i+1)
        for i in range(len(p)):
            for j in range(len(p)):
                if i!=j:
                    temp2.append(score[p[i]-1][p[j]-1])
        summ_p=sum(temp2)
        for i in range(len(q)):
            for j in range(len(q)):
                if i!=j:
                    temp1.append(score[q[i]-1][q[j]-1])
        summ_q=sum(temp1)

        answer.append(abs(summ_q-summ_p))
        temp1.clear()
        temp2.clear()
        summ_q=0
        summ_p=0
        p.clear()
        return

    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            q.append(i+1)
            dfs(x+1)
            q.pop()
            visited[i]=0

    return

dfs(0)
print(min(answer))