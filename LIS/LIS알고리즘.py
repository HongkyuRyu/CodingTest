arr = [10, 40, 20, 50, 30, 40, 60]
n = len(arr)
dp = [1] * n # 첫 길이는 1

for cur in range(1, n): 
    for prev in range(cur):
        # 증가하는 값이라면
        if arr[prev] < arr[cur]:
            # 이전 길이에 +1을 더한 값이 더 크다면 변경
            if dp[cur] < dp[prev] + 1:
                dp[cur] = dp[prev] + 1

print(dp[-1])

