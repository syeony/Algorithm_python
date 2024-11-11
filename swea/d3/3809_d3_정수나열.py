T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr=[]
    while len(arr) < N:
    # 공백 또는 줄바꿈으로 입력된 숫자를 추가
        arr.extend(map(int, input().split()))
    two = ''
    min = 0
    arr2 = list(set())

    # for i in range(N):
    #     arr2.append(arr[i])
    #     if N>1 and i+1<N:
    #         two = int(str(arr[i])+str(arr[i+1]))
    #         arr2.append(two)

    for i in range(N):
        arr2.append(arr[i])
        for j in range(i+1,N):
            if N>1 and j<N:
                arr2.append(int(''.join(map(str, arr[i:j]))))

    arr2 = sorted(arr2)

    for i in range(len(arr2)):
        if i not in arr2:
            min = i
            break
    
    print(f"#{test_case} {min}")