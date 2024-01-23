import sys
sys.stdin = open("C:\\Users\\Admin\\Desktop\\code\\input.txt", "r")

# n개의 원소로 구성된 자연수 집합이 주어지면
# 해당 집합을 두개의 부분집합으로 나눈다.
# 각각의 부분집합의 원소의 서로 합이 같으면 "yes" 아니면 "No"를 출력

def dfs(idx, sum): # 인덱스번호, 누적합
    if idx == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
        
    else:
        dfs(idx+1, sum+lst[idx])
        dfs(idx+1, sum)

if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    total = sum(lst)
    dfs(0, 0)
    print("NO")