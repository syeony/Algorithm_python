# 시간초과

T = int(input())

for test_case in range(1,T+1):
    n = int(input())

    arr = list(map(int,input().split()))
    i_stack = []
    two = []
    max = 0

    def dfs():
        global max
        if len(two) >= 2:
            mul=two[0]*two[1]
            if mul > max:
                if sorted(str(mul)) == list(str(mul)):
                    max = mul

        for i in range(len(arr)):
            if i not in i_stack:
                two.append(arr[i])
                i_stack.append(i)
                dfs()
                two.pop()
                i_stack.pop()

    dfs()

    print(f"#{test_case} {max}")
