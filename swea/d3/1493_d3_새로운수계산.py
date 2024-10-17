# 왜 최대 배열 값이 300*300으로 해야 통과과 될까...?

def star(p,q):
    arr = [[0]*300 for _ in range(300)]
    count=0
    start_x, start_y, end_x, end_y = 0, 0, 0, 0

    for i in range(1,300):
        for j in range(1,i+1):
            count+=1
            arr[j][i-j+1] = count
            # print(j, i-j+1)
            if count == p:
                start_x = j
                start_y = i-j+1
            if count == q:
                end_x = j
                end_y = i-j+1

    x = start_x+end_x
    y = start_y+end_y

    return arr[x][y]
    
    # for i in range(0,q+1):
    #     print(arr[i])


T= int(input())

for test_case in range(1,T+1):
    p,q = map(int,input().split())
    
    print(f"#{test_case} {star(p,q)}")
