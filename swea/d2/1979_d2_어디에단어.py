T = int(input())

for tc in range(1,T+1):
    n,k = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(n)]
    arr2 = list(zip(*arr))
    count = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    count+=1
                cnt = 0
        if cnt == k:
            count += 1
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr2[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    count+=1
                cnt = 0
        if cnt == k:
            count += 1

    print(f"#{tc} {count}")