# n개의 수 중 한개의 수인 M이 주어졌을 때,
# M이 몇번째에 있는지 구하여라.
import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

print(bisect.bisect_left(arr, m, 0, len(arr)-1) + 1)

# 혹은, 이분탐색 구현으로 풀이
lt = 0
rt = len(arr) - 1
while lt <= rt:
    mid = (lt + rt) // 2

    if arr[mid] == m:
        print(mid+1)
        break
    elif arr[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1



    
