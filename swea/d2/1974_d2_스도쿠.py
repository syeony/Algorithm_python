T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    arr2 = list(zip(*arr))
    result = 1       
    
    flag = False
    for i in range(9):
        if len(list(set(arr[i]))) != 9:
            result = 0
            break
        if len(list(set(arr2[i]))) != 9:
            result = 0
            break
        for j in range(9):
            li = []
            for x in range(3):
                for y in range(3):
                    li.append(arr[x][y])
            if len(list(set(li))) != 9:
                result = 0
                flag = True
                break
        if flag:
            break


    print(f"#{tc} {result}")