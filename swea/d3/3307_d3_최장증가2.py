# dp 이해가 힘들었음
# https://techblog-history-younghunjo1.tistory.com/295
# 이거보고 완벽 이해

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [1] * n

    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j]:
                dp[i] = max(dp[j]+1,dp[i])

    print(f"#{test_case} {max(dp)}")
