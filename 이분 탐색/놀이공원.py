# 놀이기구의 번호를 출력해야함

# 놀이기구 종류가 1개 인 경우 = M = 1

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = list(map(int, input().split()))


if n < m:
    print(n)
else:
    start, end = 0, max(times) * n # 30 * 20억
    t = 0 # 아이들을 모두 태울수 있는 시간
    while start <= end:
        mid = (start + end) // 2
        # 처음 1초에는 M명의 놀이기구에, 아이들이 탑승했으므로
        # cnt = 놀이기구 탑승한 아이들의 숫자
        cnt = m
        for i in range(m):
            # 특정 시간동안 M개의 놀이기구에 탑승한 아이들의 숫자
            cnt += (mid // times[i])

        # 탑승한 아이들의 숫자가 N보다 크거나 같은 경우
        if cnt >= n:
            t = mid
            end = mid - 1
        else:
            start = mid + 1

    # t=> 아이들을 모두 태울 수 있는 시간
    # 제일 마지막에 탑승한 놀이기구의 번호를 알아야함
    # 놀이기구 탑승 인원이 N명이 될 때의 놀이기구 번호를 알아야하므로
    # t-1(분)에 탑승한 아이들의 숫자를 계산
    cnt = m
    for i in range(m):
        cnt += (t-1) // times[i]
    
    # 이제, t(분)이 될때 탑승한 아이들의 숫자를 계산
    for i in range(m):
        if t % times[i] == 0: # t분이 되었을 때 탑승한 아이
            cnt += 1
        if cnt == n:
            print(i+1) # idx때문
            break

