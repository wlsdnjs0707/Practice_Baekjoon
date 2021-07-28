# 스도쿠

board=[]

for i in range(9):
    board.append(list(map(int,input().split())))

def horizontal():
    zero_count=0
    summ=0
    number_set=set()

    # 가로 채우기
    for i in range(9):
        
        for j in range(9):
            if board[i][j]==0:
                zero_count+=1
        
        if zero_count==1:
            for k in range(9):
                if board[i][k]!=0:
                    number_set.add(board[i][k])
                    summ+=board[i][k]
            for k in range(9):
                if board[i][k] not in number_set:
                    board[i][k]=45-summ

        zero_count=0
        summ=0
        number_set.clear()
    return

def vertical():
    zero_count=0
    summ=0
    number_set=set()
    # 세로 채우기 
    for i in range(9):

        for j in range(9):
            if board[j][i]==0:
                zero_count+=1
        
        if zero_count==1:
            for k in range(9):
                if board[k][i]!=0:
                    number_set.add(board[k][i])
                    summ+=board[k][i]
            for k in range(9):
                if board[k][i] not in number_set:
                    board[k][i]=45-summ

        zero_count=0
        summ=0
        number_set.clear()

    return

def three():
    cord=[[3,3],[6,3],[9,3],[3,6],[6,6],[9,6],[3,9],[6,9],[9,9]]

    zero_count=0
    number_set=set()
    summ=0

    for c in range(9):
        x=cord[c][0]
        y=cord[c][1]

        for i in range(x-3,x):
            for j in range(y-3,y):
                if board[i][j]==0:
                    zero_count+=1
        
        if zero_count==1:
            for i in range(x-3,x):
                for j in range(y-3,y):
                    if board[i][j]!=0:
                        number_set.add(board[i][j])
                        summ+=board[i][j]    
            for i in range(x-3,x):
                for j in range(y-3,y):
                    if board[i][j] not in number_set:
                        board[i][j]=45-summ

for i in range(3):
    horizontal()
    vertical()
    three()
    
for i in range(9):
    for j in range(9):
        if j==8:
            print(board[i][j])
        else:
            print(board[i][j],end=' ')