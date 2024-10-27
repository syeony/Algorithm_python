T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())  # 갯수, 최대 부피
    arr = [list(map(int, input().split())) for _ in range(n)]  # 부피, 가치

    # DP 테이블 초기화 (최대 부피 k까지 고려)
    dp = [0] * (k + 1)

    # 각 물건에 대해 반복
    for i in range(n):
        volume, value = arr[i]
        # 부피를 뒤에서부터 순회하면서 물건을 담을 수 있는지 판단
        for j in range(k, volume - 1, -1):
            dp[j] = max(dp[j], dp[j - volume] + value)

    print(f"#{test_case} {dp[k]}")
