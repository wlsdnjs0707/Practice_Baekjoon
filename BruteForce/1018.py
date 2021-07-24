# 체스판 다시 칠하기

n,m = map(int,input().split())

chess=[]
chess_cut=[]
count=0
count_list=[]

for i in range(8):
    chess_cut.append([0 for j in range(8)])

for i in range(n):
    chess.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        for a in range(i,i+8):
            for b in range(j,j+8):
                if i==0 and j==0:
                    chess_cut[a][b]=chess[a][b]
                elif i==0:
                    chess_cut[a][b-j]=chess[a][b]
                elif j==0:
                    chess_cut[a-i][b]=chess[a][b]
                else:
                    chess_cut[a-i][b-j]=chess[a][b]

        for a in range(8):
            for b in range(8):
                if chess_cut[0][0]=='W':
                    if a%2==0 and b%2==0:
                        if chess_cut[a][b]=='B':
                            count+=1
                    elif a%2==0 and b%2==1:
                        if chess_cut[a][b]=='W':
                            count+=1
                    elif a%2==1 and b%2==0:
                        if chess_cut[a][b]=='W':
                            count+=1
                    elif a%2==1 and b%2==1:
                        if chess_cut[a][b]=='B':
                            count+=1
                elif chess_cut[0][0]=='B':
                    if a%2==0 and b%2==0:
                        if chess_cut[a][b]=='W':
                            count+=1
                    elif a%2==0 and b%2==1:
                        if chess_cut[a][b]=='B':
                            count+=1
                    elif a%2==1 and b%2==0:
                        if chess_cut[a][b]=='B':
                            count+=1
                    elif a%2==1 and b%2==1:
                        if chess_cut[a][b]=='W':
                            count+=1
        count_list.append(count)
        count=0

print(count_list)
print(min(count_list))