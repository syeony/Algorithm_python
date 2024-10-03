import sys
sys.stdin = open("/Users/ohseungyeon/Documents/swea/d3/1209_input.txt", "r")

for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # 2차원 배열 입력받기

    max_sum, right_down, left_up = 0, 0, 0

    for i in range(0,100):
        right_down += arr[i][i]
        left_up += arr[i][99-i]

    max_sum = max(right_down, left_up)

    for i in range(0,100):
        row_sum = 0
        col_sum = 0
        for j in range(0,100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        
        max_sum = max(max_sum, row_sum, col_sum)

    print(f"#{test_case} {max_sum}")