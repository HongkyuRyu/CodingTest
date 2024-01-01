# (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

prefixSum = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]

# 부분합 구할 횟수 K
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(prefixSum[x][y] - prefixSum[i-1][y] - prefixSum[x][j-1] + prefixSum[i-1][j-1])
    

