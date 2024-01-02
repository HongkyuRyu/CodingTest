# 적어도 M미터의 나무를 집에 가져가기 위해 설정해야할 높이의 최댓값
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))
s = 0
e = max(height)

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in height:
        if i >= mid:
            cnt += (i - mid)
        else:
            continue
    if cnt >= m:
        s = mid + 1
    else:
        e = mid - 1
print(e)
