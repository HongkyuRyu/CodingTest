# 랜선의 최대 길이를 출력
# 랜선의 개수 K, 필요한 랜선의 개수 N

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

lt = 1 # 1cm
rt = max(lines) # 2^31이하의 자연수

while lt <= rt:
    mid = (lt + rt) // 2
    temp = 0 # 기준길이로 나누었을 때, 나누어지는 전선의 갯수
    for line in lines:
        temp += (line // mid) 
    if temp >= n: # 필요한 전선의 갯수
        # 더 많이 쪼개졌다는 것은, 값이 아직 작다는 뜻이니까
        lt = mid + 1
    else:
        rt = mid - 1
print(rt)