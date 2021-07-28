# N-Queen

# 한 행(Row)마다 하나의 퀸이 들어가야한다.
# 한 열(Column)마다 하나의 퀸이 들어가야한다.
# 대각선에 하나의 퀸이 들어가야한다.

# 행 판정
# 한 행에 퀸을 위치시키면 다음행으로 패스

# 열 판정
# 이전 퀸과 같은열에 위치하면 패스

# 대각선 판정
# 1. 음의방향 대각선
# (행-열)의 절대값이 같으면 같은 대각선상에 존재한다.
# 2. 양의방향 대각선
# (행+열)의 값이 같으면 같은 대각선상에 존재한다.

n=int(input())
count=0 # 해의 개수

col=set() #열 집합
posDiag=set() #(r+c) 집합
negDiag=set() #(r-c) 집합

def backtrack(r): #행 별로 판정
    global count
    if r==n:      #행 끝까지 내려왔을때
        count+=1
        return

    for c in range(n):
        # 열,대각선 판정
        if c in col or (r+c) in posDiag or (r-c) in negDiag:
            continue
        
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
            
        backtrack(r+1)

        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)

backtrack(0) # 맨 위부터 시작
print(count)