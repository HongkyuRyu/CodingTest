# 기준선 이상은 기준선금액으로 계산
# 기준선 이하금액은 원래 금액으로 계산

# 최대로 예산 배정하고자 함
# 범위: 0 ~ 가장 큰 금액

# 기준선으로 값을 계산했을 때, 국가예산 총액과 같아질 때까지 계산
# 기준선을 출력

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
money = int(input())

lo = 0
ro = max(arr)

answer = 0

while lo <= ro:
    mid = (lo + ro) // 2 # 기준선
    temp = 0
    for i in range(len(arr)):
        if arr[i] >= mid: # 기준선보다 클 경우는
            temp += mid
        else:
            temp += arr[i]
    
    if temp > money: # 예산 총액보다 커질 경우
        ro = mid - 1
    else:
        answer = mid
        lo = mid + 1

print(answer)

