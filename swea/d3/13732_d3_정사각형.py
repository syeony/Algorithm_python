T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    i_jul,j_jul = 0,0
    result = 'no'

    flag = False
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                i_jul = i
                j_jul = j
                flag = True
                break
        if flag:
            break

    i_count = arr[i_jul].count('#')

    # print(i_jul,j_jul,i_count)

    flag = False
    for i in range(i_jul, i_jul+i_count):
        for j in range(j_jul, j_jul+i_count):
            if arr[i][j] == '.':
                flag = True
                break
        if flag:
            break
    else:
        result = 'yes'

    cnt = 0
    for i in range(n):
        cnt+=arr[i].count('#')
    
    if cnt != i_count*i_count:
        result = 'no'

    print(f"#{tc} {result}")

