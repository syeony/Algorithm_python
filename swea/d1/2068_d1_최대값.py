# min(), max()는 파이썬 내장 함수라서 따로 import해올 필요 없다

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    max_value = max(arr)

    print(f"#{test_case} {max_value}")