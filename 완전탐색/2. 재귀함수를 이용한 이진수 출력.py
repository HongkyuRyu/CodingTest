import sys
sys.stdin = open("C:\\Users\\Admin\\Desktop\\code\\input.txt", "r")

def dfs(x):
    if x==0:
        return
    else:
        print(x%2, end='')
        dfs(x//2)


if __name__ == "__main__":
    n = int(input())
    dfs(n)