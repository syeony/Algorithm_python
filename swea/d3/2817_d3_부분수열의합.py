T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    # sum = 0
    # first_arr = []
    # second_arr = [[]]

    # def dfs():
    #     global sum
    #     global first_arr

    #     if sum == K:
    #         sorted_arr = sorted(first_arr)
    #         if sorted_arr not in second_arr:
    #             second_arr.append(sorted_arr)

    #     for i in range(N):
    #         if i not in first_arr:
    #             first_arr.append(i)
    #             sum += arr[i]
    #             dfs() #재귀함수
    #             sum -= arr[i]
    #             first_arr.pop() #백트래킹

    # dfs()
    # del(second_arr[0])

    # print(f"#{test_case} {len(second_arr)}")

    count = 0  

    def dfs(index, sum):
        global count

        if sum == K:
            count += 1
            return

        # 배열 끝까지 탐색했으면 종료
        if index == N:
            return

        # 현재 원소를 포함하는 경우
        dfs(index + 1, sum + arr[index])

        # 현재 원소를 포함하지 않는 경우
        dfs(index + 1, sum)

    dfs(0, 0)

    print(f"#{test_case} {count}")
