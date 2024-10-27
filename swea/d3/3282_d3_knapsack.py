# 시간초과

T = int(input())

for test_case in range(1,T+1):
    n,k = map(int,input().split()) # 갯수, 부피

    arr = [list(map(int,input().split())) for _ in range(n)] # 부피, 가치
    max_c = 0

    def dfs(index, v, c):
        global max_c
        if v <= k:
            max_c = max(max_c, c)

        for i in range(index,n):
            dfs(i+1, v+arr[i][0], c+arr[i][1])

    dfs(0,0,0)

    print(f"#{test_case} {max_c}")


