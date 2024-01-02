import bisect
arr = [4, 3, 2, 2, 4, 4, 1, 1, 1]
arr.sort()
print(arr)
def lower_bound(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
print(lower_bound(0, len(arr)-1, 4))
print(bisect.bisect_left(arr, 4, 0, len(arr)-1))

