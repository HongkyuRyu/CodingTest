import sys
sys.stdin = open("C:\\Users\\Admin\\Desktop\\code\\input.txt", "r")

# 자연수 n이 주어졌을 때, 1부터 n까지를 원소로 하는 부분집합 출력
# 공집합 출력x

def dfs(v):
    if v == n+1:
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end=" ")
            print()
    else:
        check[v] = 1
        dfs(v+1)
        check[v] = 0
        dfs(v+1)


if __name__ == "__main__":
    n = int(input())
    check = [0] * (n+1)
    dfs(1)
