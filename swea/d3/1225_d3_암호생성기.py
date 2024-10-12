for test_case in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))

    while arr[-1] != 0:
        for i in range(1,6):
            arr[0] = arr[0]-i
            if arr[0] <= 0:
                del(arr[0])
                arr.append(0)
                break
            arr.append(arr[0])
            del(arr[0])

    print(f"#{test_case}", end=' ')
    for i in arr:
        print(i, end=' ')