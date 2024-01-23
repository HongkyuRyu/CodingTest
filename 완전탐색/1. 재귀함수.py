import sys
sys.stdin = open("C:\\Users\\Admin\\Desktop\\code\\input.txt", "r")

def dfs(x):
    if x > 0:
        print(x)
        dfs(x-1)

if __name__ == "__main__":
    n = int(input())
    dfs(n)