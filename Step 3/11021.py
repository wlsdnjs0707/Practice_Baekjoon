# A+B-7

case_list = []

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    case_list.append(a+b)

for i in range(len(case_list)):
    print("Case #{0}: {1}".format(i+1,case_list[i]))