T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = input().split()
    left_arr = []
    right_arr = []
    result_arr = []

    for i in range(n):
        if n%2 == 0:
            if i < n//2:
                left_arr.append(arr[i])
            else:
                right_arr.append(arr[i])
        else:
            if i <= n//2:
                left_arr.append(arr[i])
            else:
                right_arr.append(arr[i])
    
    for i in range(n//2): # 0 1 2
        result_arr.append(left_arr[i])
        result_arr.append(right_arr[i])

    if n%2 != 0:
        result_arr.append(left_arr[-1])

    print(f"#{tc}", end=' ')
    for i in range(n):
        print(f"{result_arr[i]}", end = ' ')

    print("")