import statistics

# import sys
# sys.stdin = open("/Users/ohseungyeon/Documents/swea/d2/1204_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # num = statistics.mode(arr) # momory error

    arr_2 = [0] * 101
    for i in arr:
        arr_2[i] += 1

    max_value = max(arr_2)  # 배열에서 가장 큰 값 찾기
    # num = arr_2.index(max_value)  # 그 값의 인덱스 찾기

    for i in range(len(arr_2)-1, -1, -1):
        if max_value == arr_2[i]:
            print(f"#{N} {i}")
            break
