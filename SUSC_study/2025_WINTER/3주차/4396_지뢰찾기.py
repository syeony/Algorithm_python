n = int(input())

arr1 = [list(input().strip()) for _ in range(n)]
arr2 = [list(input().strip()) for _ in range(n)]

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

flag = False # 지뢰 안밟았을때

for i in range(n):
    for j in range(n):

        cnt = 0
        if arr2[i][j]=='x':
            if arr1[i][j]=='*': # 지뢰 밟았을때 신호 바꿔놓음
                flag = True

            for x in range(8):
                nx = i+dx[x]
                ny = j+dy[x]
                
                if nx>=n or ny>=n or nx<0 or ny<0:
                    continue

                if arr1[nx][ny]=='*':
                    cnt+=1
            
            if cnt >=1:
                arr2[i][j]=str(cnt)
                
            else:
                arr2[i][j]='0'

if flag==True:
    for i in range(n):
        for j in range(n):
            if arr1[i][j]=='*':
                arr2[i][j]='*'

for i in range(n):
       print(''.join(arr2[i]))
