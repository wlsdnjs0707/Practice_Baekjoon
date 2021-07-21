# 손익분기점
# a = 고정비용, b = 가변비용, c = 가격


a,b,c = map(int,input().split())

count = 1

# if b>=c:
#     print(-1)
# else:
#     while a+b*count>=c*count:
#         count+=1
#     print(count)

if b>=c:
    print(-1)
else:
    print(int(a/(c-b))+1)
