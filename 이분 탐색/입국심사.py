"""
범위: 심사를 하는데 걸리는 총 시간
1분 ~ max(times) * n (n명이 모두 가장 긴 시간이 소요되는 상황)

mid = 모든 심사위원들에게 주어진 시간
for i in times: 
    temp += mid // i

temp = 모든 심사위원들이 mid분동안 심사한 사람의 수


mid분 동안 심사한 사람의 수가
1. 심사받아야할 사람의 수(n)보다 크거나 같을 경우는 
- 시간이 충분했던 것
- 주어진 시간을 줄이고(end = mid - 1)
2. 심사받아야할 사람의 수(n)보다 작은 경우는
- 시간이 부족했던 것
- start = mid + 1
"""
n = 6
times = [7, 10]

def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

print(solution(n, times))



