arr = [10, 40, 20, 50, 30, 40, 60]
n = len(arr)
# 수열의 첫번째 값 설정
lis = [arr[0]]


# 이분 탐색 알고리즘
def binary_search(target, lis):
    start, end= 0, len(lis)-1
    while start < end:
        mid = (start + end) // 2

        if lis[mid] == target:
            return mid

        elif lis[mid-1] < target < lis[mid]: 
            return mid

        elif target < lis[mid]:
            end = mid - 1
        
        else:
            start = mid + 1
    return start


for i in range(1, n):
    target = arr[i]
    # 타겟이 더 크다면 LIS에 추가
    if lis[-1] < target:
        lis.append(target)
    # 타겟이 더 작을 경우 이분탐색을 통해 LIS 갱신
    else:
        idx = binary_search(target, lis)
        lis[idx] = target

print(len(lis))

