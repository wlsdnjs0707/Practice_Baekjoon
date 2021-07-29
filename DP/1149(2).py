# RGB거리
# 동적 계획법 사용

n = int(input())

rgb=[]

for i in range(n):
    rgb.append(list(map(int,input().split())))

for i in range(1,n):
    rgb[i][0] = min(rgb[i-1][1],rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0],rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0],rgb[i-1][1]) + rgb[i][2]

    # 2번째 집부터 규칙에 맞는 최소값들을 rgb에 저장
    # 이전 까지의 최소비용 + 해당 인덱스 집의 비용

print(min(rgb[n-1]))