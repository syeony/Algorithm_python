# 답 참고

T = int(input())

for test_case in range(1,T+1):
    n, l = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    score_max = 0

    def dfs(index, score_sum, calorie_sum):
        global score_max

        if calorie_sum <= l:
            score_max = max(score_max, score_sum)

        for i in range(index, n):
            dfs(i+1, score_sum + arr[i][0], calorie_sum + arr[i][1])

    dfs(0,0,0)
        
    print(f"#{test_case} {score_max}")
