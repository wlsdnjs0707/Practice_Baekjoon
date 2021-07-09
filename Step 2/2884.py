# 알람 시계

h,m = map(int,input().split())

if m<45 :
    if h==0:
        print("23 %d" %(m+15))
    else:
        print("{0} {1}".format(h-1,m+15))
elif h==0:
    print("23 {0}".format(m-45))
else:
    print("{0} {1}".format(h-1,m-45))

