# 회의실 하나에서 최대한 회의를 많이 해야 한다.
import sys
input = sys.stdin.readline

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))

# end time
et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e # 회의 끝나는 시간 업데이트
        cnt += 1 
print(cnt)

