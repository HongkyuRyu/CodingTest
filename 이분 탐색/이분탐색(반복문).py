data = [3, 5, 7, 9, 8, 1]
def binary_search(target):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        
        # target이 mid값보다 작으면
        # 왼쪽 탐색
        elif data[mid] > target:
            end = mid - 1
        
        # target이 mid값보다 크다면
        # 오른쪽 탐색
        else:
            start = mid + 1
    return

print(binary_search(5))

        
