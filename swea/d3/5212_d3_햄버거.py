T = int(input())

for test_case in range(1,T+1):
    n, l = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # sorted_arr = sorted(arr, key = lambda x: x[0], reverse=True)

    score_arr = []
    score_sum = 0
    score_max = 0
    calorie_sum = 0

    def dfs():
        global calorie_sum
        global score_sum
        global score_arr
        global score_max

        if calorie_sum <= l:
            if score_max < sum(score_arr):
                score_max = sum(score_arr)
            
            
        for i in range(n):
            if i not in score_arr:
                score_arr.append(arr[i][0])
                score_sum += arr[i][0]
                calorie_sum += arr[i][1]
                dfs() #재귀함수
                score_arr.pop() #백트래킹
                score_sum -= arr[i][0]
                calorie_sum -= arr[i][1]

    dfs()
        
    print(f"#{test_case} {score_max}")
