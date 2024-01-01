import sys
input = sys.stdin.readline

n,k,q,m = map(int, input().split())

# 1. 조는 학생을 먼저 체크한다.
sleep = [0]*(n+3)
check = [0]*(n+3)

for i in map(int, input().split()):
    sleep[i] = 1
# 2. 출석 번호 받은 사람 체크
for i in map(int, input().split()):
    if sleep[i]: 
        continue
    for j in range(i, n+3, i): # 배수
        if not sleep[j]:
            check[j] = 1
# 누적합  = 출석한 학생들의 합
prefix = [check[0]]
for i in range(1, n+3):
    prefix.append(prefix[-1]+check[i]) 

#print(prefix)
#  결석학생수 = 구간전체출석학생 수 - 누적합(구간 마지막값) - 누적합(구간 시작값-1)
for _ in range(m):
    s, e = map(int, input().split()) 
    print(e-s+1 - (prefix[e]-prefix[s-1])) 