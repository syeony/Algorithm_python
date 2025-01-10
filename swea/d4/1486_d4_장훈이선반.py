# 보자마자 완전탐색 문제라는건 알았으나 dfs 다 까먹어서 다시 찾아봄
# 내가 푼게 아님

T = int(input())

for tc in range(1,T+1):

    def dfs(index,sum):
        global answer

        # 가지치기라는데 굳이 안넣어도 패스됨...
        # if answer<=sum:
        #     return
        
        # 종료조건(if문을 저렇게 따로 쓴데는 이유가 있다)
        if index==n:
            if b<=sum<answer:
                answer = sum
            return

        dfs(index+1,sum)
        dfs(index+1,sum+arr[index])

    n,b = map(int,input().split())
    arr = list(map(int,input().split()))

    answer = 200000
    dfs(0,0)
    print(f"#{tc} {answer-b}")