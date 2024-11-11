T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    sum_max = 0

    for i in range(N-1):
        for j in range(i+1,N):
            if arr[i]+arr[j]<=M and arr[i]+arr[j]>sum_max:
                sum_max = arr[i]+arr[j]

    if sum_max == 0:
        sum_max = -1

    print(f"#{test_case} {sum_max}")