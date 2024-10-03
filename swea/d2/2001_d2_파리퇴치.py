T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0

    # 4중 for문 -> 더 간단한 방법은 없을까...?
    for i in range(N):
        for j in range(N):
            sum = 0
            for x in range(M):
                for y in range(M):
                    if x+i < N and y+j < N:
                        sum += arr[x+i][y+j]
            if sum > max:
                max = sum
            else:
                pass
    
    print(f"#{test_case} {max}")