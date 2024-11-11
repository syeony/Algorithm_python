T = int(input())

for tc in range(1,T+1):
    a, b, n = map(int,input().split())
    mi = min(a,b)
    ma = max(a,b)
    num = 0
    arr = []

    while mi<=n: 
        # 이거 동시에 저장하는게 키포인트
        mi, ma = mi + ma, max(mi, ma)
        num += 1
    
    arr.append(num)

    for i in range(len(arr)):
        print(arr[i])