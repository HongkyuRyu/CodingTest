import sys
input = sys.stdin.readline

# 랜선의 개수, 필요한 랜선의 개수( = 같은 길이)
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

left = 1
right = max(lines)

while left <= right:
    mid = (left + right) // 2
    l = 0
    for i in lines:
        l += (i // mid)
    if l >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)

