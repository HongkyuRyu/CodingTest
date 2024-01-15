# 각 마구간에는 한마리의 말만 넣을 수 있다.
# 가장 가까운 두 말의 거리가 최대가 되게 말을 배치

# N개의 마구간이 수직선상에 위치
# C마리의 말

# 가장 가까운 두 말의 최대 거리 출력

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
magugans = list(int(input()) for _ in range(n))
magugans.sort()

# 1, 2, 4, 8, 9 좌표


