T1 = int(input())

for test_case in range(1, T1 + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    sum=0   
    max = arr[-1]

    for i in range(len(arr)-2, -1, -1):
        # print("max: ", max, "arr[i]: ", arr[i]) # 테스트
        if max > arr[i]:
            sum += (max-arr[i])
        elif max == arr[i]:
            pass
        else: 
            max = arr[i]

    print(f"#{test_case} {sum}")
