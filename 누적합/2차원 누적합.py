n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def prefix_sum(n, m):
    prefixSum = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]
    return prefixSum

s = prefix_sum(n, m)

