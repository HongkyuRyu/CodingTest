#(2, 2)와 (4, 5)라는 지점에 대해 밝기 평균을 구하려면
# 해당 구간의 누적합 / 해당 구간의 칸의 수 

import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

prefixSum = [[0] * (c+1) for _ in range(r+1)] 
for i in range(1, r+1):
    for j in range(1, c+1):
        prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    cnt = (r2-r1+1) * (c2-c1+1)
    print((prefixSum[r2][c2] - prefixSum[r1-1][c2] - prefixSum[r2][c1-1] + prefixSum[r1-1][c1-1]) // cnt)

    
