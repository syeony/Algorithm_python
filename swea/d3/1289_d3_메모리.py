# 10분 컷

T = int(input())

for test_case in range(1,T+1):
    num = int(input())

    arr = list(map(int,str(num)))
    sum = 0

    if arr[0] == 1:
        sum += 1
    
    if len(arr) <= 1:
        pass
    else:
        for i in range(1,len(arr)):
            if arr[i] != arr[i-1]:
                sum += 1

    print(f"#{test_case} {sum}")
