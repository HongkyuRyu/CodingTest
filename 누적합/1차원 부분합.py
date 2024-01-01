def prefix_sum(n):
    prefixSum = [0] * n
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i-1] + arr[i]
    return prefixSum


n = int(input())
arr = list(map(int, input().split()))
# 구하고자 하는 범위
i, j = map(int, input().split())


print("arr")
print(arr)
print()

s = prefix_sum(n)
print("prefixSum")
print(s)
print()


# 부분합
partSum = s[j] - s[i-1]
print(partSum)

