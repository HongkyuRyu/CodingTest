# sorting 조건
# 무거운 지원자 > 키 큰 지원자
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    h, w = map(int, input().split())
    lst.append((h, w))
lst.sort(key=lambda x: (-x[1], -x[0]))

height = lst[0][0]
weight = lst[0][1]
cnt = 0
for h, w in lst:
    # 다음 선수가 현재 선수보다 키가 크거나, 무거우면
    if h >= height and w>= weight:
        height, weight = h, w
    elif h >= height and w < weight:
        cnt += 1
    elif h < height and w >= weight:
        cnt += 1
        weight = w
print(cnt)

