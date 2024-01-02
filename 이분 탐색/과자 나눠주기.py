# 최대한 긴 과자를 나누어주려고 한다.
# 같은 길이의 막대 과자 

# 조카 1명에게 줄 수 있는 막대과자의 최대 길이
import sys
input = sys.stdin.readline

# 조카의수m, 과자의수n
m, n = map(int, input().split())
# 과자 n개의 길이
snack = list(map(int, input().split()))

s = 1 # 막대과자의 길이는 1이상(양의 정수)
e = max(snack)

while s <= e:
    mid = (s + e) // 2
    length = 0
    if mid == 0:
        length = 0
        break
    for i in snack:
        if i >= mid:
            length += (i // mid)
    if length >= m:
        s = mid + 1
        
    else:
        e = mid - 1 

print(e)
