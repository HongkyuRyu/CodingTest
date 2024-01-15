"""
DVD 총 N개의 곡이 들어가야 한다.
# 곡의 순서는 그대로 유지되어야 한다.
# DVD의 크기(녹화 가능 길이)는 최소로 하려고 한다.
"""
import sys
input = sys.stdin.readline

# n개의 곡, m개의 DVD
n, m = map(int, input().split())
# 곡의 길이 
songs = list(map(int, input().split()))

# 곡의 길이 // 기준값(DVD에 녹화되는 시간) = 필요한 DVD의 갯수
# 시간을 범위로 선정해야한다.
lt = 1 # 1분
rt = 1000 * 10000 # 최대 시간
answer = 0

while lt <= rt:
    # 기준시간
    mid = (lt + rt) // 2
    required = 0 # 필요한 DVD의 갯수
    for song in songs:
        required += (song // mid)
    # 필요한 DVD의 갯수 >= m
    if required >= m:
        answer = mid
        # DVD의 용량이 적은현상
        lt = mid + 1
    else:
        rt = mid - 1

# 기준 시간 보다 앞에 있는 것들의 합
result = 0
for song in songs:
    if answer < song:
        result += song
print(result)

