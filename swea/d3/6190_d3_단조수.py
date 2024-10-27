# 아 문제 잘못 이해함

T = int(input())

for test_case in range(1,T+1):
    n = int(input())

    arr = list(map(int,input().split()))
    new_arr = []

    for i in arr:
        num = list(map(int, str(i)))
        if len(num) == 1:
            new_arr.append(i)
        else:
            new_arr.append(i)
            for j in range(1,len(num)):
                if num[j] < num[j-1]:
                    new_arr.pop()
                    break
    if len(new_arr) == 0:
        result = -1
    else:
        new_arr = sorted(new_arr)
        a = new_arr[-1]
        new_arr.pop()
        b = new_arr[-1]

        result = a*b
    print(f"#{test_case} {result}")
            