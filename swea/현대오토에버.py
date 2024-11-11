# 23 2 = 6 (2,2,4,4,6) 22
# 9 2 = 3
# 10 1 = 5 (1,1,2,2,3) 9

T = int(input())

for tc in range(1, T+1):
    distance, startspeed = map(int,input().split())
    arr = []
    i = 1
    while True:
        arr.append(startspeed*i)
        if sum(arr) > distance-1:
            arr.pop()
            break
        arr.append(startspeed*i)
        if sum(arr) > distance-1:
            arr.pop()
            break
        i += 1
    
    if sum(arr) < distance-1:
        arr.append(distance-1-sum(arr))

    print(f"#{tc} {len(arr)} {arr}")