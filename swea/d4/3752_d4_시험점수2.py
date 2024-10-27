T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split())) # 2 3 5 -> 5 5

    sum_arr = [0]

    for i in arr: # set으로 중복제거해줘야
        sum_arr = list(set(sum_arr))
        for j in range(len(sum_arr)): # 여기서 인덱스 에러가 안 남
            sum_arr.append(i+sum_arr[j])

    print(f"#{test_case} {len(set(sum_arr))}")