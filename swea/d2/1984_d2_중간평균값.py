# 반올림 round

T = int(input())

for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))
    result = sum(arr)/len(arr)
    print(f"#{tc} {round(result)}")