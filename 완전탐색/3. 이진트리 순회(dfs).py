import sys
sys.stdin = open("C:\\Users\\Admin\\Desktop\\code\\input.txt", "r")

def dfs(v):
    if v > 7:
        return
    else:
        print(v, end="")
        dfs(v*2)
        dfs(v*2+1)


if __name__ == "__main__":
    dfs(1)