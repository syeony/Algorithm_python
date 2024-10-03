for test_case in range(1,11):
    T = int(input())

    arr = list(map(int, input().split()))
    sum = 0
    for i in range(2, len(arr) - 2): # 배열 2번째값부터 -3번째 값만 보기
        if arr[i]>arr[i-1] and arr[i]>arr[i-2] and arr[i]>arr[i+1] and arr[i]>arr[i+2]:
            max_arr = max(arr[i-1], arr[i-2], arr[i+1], arr[i+2]) # 배열 특정 요소들에서의 최대값 구하기
            sum += (arr[i]-max_arr)
        else:
            pass

    print(f"#{test_case} {sum}")