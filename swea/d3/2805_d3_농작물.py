T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    sum = 0

    for i in range(n):
        start= abs((n+1)//2-(i+1)) 
        end= (n//2)+(i*1) 
        if end >= n:
            end = n+n//2-(i+1)
        for j in range(start, end+1):
            sum += arr[i][j]

    print(f"#{test_case} {sum}")
