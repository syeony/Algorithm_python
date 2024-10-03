# statistics는 평균 (mean), 중위값 (median), 최빈값 (mode) 사용 가능

import statistics

T = int(input())

arr = list(map(int, input().split()))
mid = statistics.median(arr)

print(mid)