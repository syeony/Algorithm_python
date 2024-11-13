# 이중 for문은 시간초과
# 답 봄 DP?

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    maxnum = min(arr) # 가장 큰 수가 음수일 수도 있으니까
    currentsum = 0

    for i in range(n):
        currentsum = max(currentsum+arr[i], arr[i]) #이전에 더한값+현재값 보다 현재값이 더 크면 체인지
        maxnum = max(maxnum, currentsum)
    
    print(f"#{tc} {maxnum}")