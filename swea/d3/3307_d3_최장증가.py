T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    max_su2 = 0

    for i in range(len(arr)-1):
        max_su = arr[i]
        su = 1
        for j in range(i+1,len(arr)):
            if arr[j]>max_su:
                # print(arr[j], end=' ')
                su += 1
                max_su = arr[j]

        max_su2 = max(max_su2, su)
        
    print(f"#{test_case} {max_su2}")
