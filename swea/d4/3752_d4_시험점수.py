# 완전탐색, 재귀, dfs
# 시간초과

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    arr2=[]
    sum_arr = [0]
    new_arr = [0]
    s = 0

    def su(arr):
        global s
        s = sum(new_arr)

        if s not in sum_arr:
            sum_arr.append(s)

        for i in range(n):
            if i not in arr2:
                arr2.append(i)
                index = arr2[-1]
                new_arr.append(arr[index])
                su(arr)
                arr2.pop() #dfs의 특징인 백트래킹
                new_arr.pop()
                
        return len(sum_arr)

    print(f"#{test_case} {su(arr)}")

