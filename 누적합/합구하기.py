import sys
input = sys.stdin.readline


# def prefixSum(n, arr):
#     prefix = [0] * (n+1)
#     prefix[0] = arr[0]
#     for i in range(1, n):
#         prefix[i] = prefix[i-1] + arr[i]
#     return prefix

n = int(input())
arr = list(map(int, input().split()))

# 함수를 호출하지 말고, 바로 작성
# 인덱스 조심
prefix = [arr[0]]
for i in range(1, n+1):
    prefix.append(prefix[i-1] + arr[i-1])

m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])


