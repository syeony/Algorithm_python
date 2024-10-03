# 올림 = ceil, 내림 = floor, 반올림(사사오입) = round

import statistics

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    average = statistics.mean(arr)
    result = round(average)

    print(f"#{test_case} {result}")