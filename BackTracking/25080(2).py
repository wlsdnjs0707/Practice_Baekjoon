# 스도쿠
# 백트래킹 알고리즘 사용

sudoku = [list(map(int,input().split())) for _ in range(9)]

zeros = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j]==0]

# 들어갈 수 있는 숫자만 거르는 함수
def check(i,j):
    number = [1,2,3,4,5,6,7,8,9]

    # 가로 세로에 같은 숫자가 있는지 Check
    for k in range(9):
        if sudoku[i][k] in number:
            number.remove(sudoku[i][k])
        if sudoku[k][j] in number:
            number.remove(sudoku[k][j])
    
    # 3*3칸에 같은 숫자가 있는지 Check
    i//=3
    j//=3
    for p in range(i*3,i*3+3):
        for q in range(j*3,j*3+3):
            if sudoku[p][q] in number:
                number.remove(sudoku[p][q])
    
    return number

flag = False

def dfs(x):

    global flag

    if flag:
        return

    if x==len(zeros):
        for row in sudoku:
            print(*row)
        flag = True
        return
    else:
        (i,j)=zeros[x]
        number=check(i,j)

        for num in number:
            sudoku[i][j]=num
            dfs(x+1)
            sudoku[i][j]=0

dfs(0)