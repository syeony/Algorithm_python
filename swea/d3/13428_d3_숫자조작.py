T = int(input())

for test_case in range(1,T+1):
    num = int(input())
    arr = list(map(int,str(num)))

    max_min = []
    max_min.append(num)

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            if arr[0] == 0:
                pass
            else:
                max_min.append(int(''.join(map(str,arr))))
            arr = list(map(int,str(num)))

    print(f"#{test_case} {min(max_min)} {max(max_min)}")
