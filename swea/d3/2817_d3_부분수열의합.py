# 답 참고

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

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
