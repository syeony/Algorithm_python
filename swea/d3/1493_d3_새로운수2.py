def star(p,q):
    count,n=0,1
    start_x, start_y, end_x, end_y = 0, 0, 0, 0

    while count < q:
        
        for i in range(1,n+1):
            count += 1
            if count == p:
                start_x = i
                start_y = n-i+1
            if count == q:
                end_x = i
                end_y = n-i+1
        n+=1

    x = start_x+end_x
    y = start_y+end_y

    temp_x,temp_y,count,n = 0,0,0,1

    while True:
        
        for i in range(1,n+1):
            count += 1
            temp_x = i
            temp_y = n-i+1
            if x == temp_x and y == temp_y:
                return count
        n+=1

    # print(start_x,start_y,end_x,end_y)
    # for i in range(0,q+1):
    #     print(arr[i])


T= int(input())

for test_case in range(1,T+1):
    p,q = map(int,input().split())
    
    print(f"#{test_case} {star(p,q)}")
