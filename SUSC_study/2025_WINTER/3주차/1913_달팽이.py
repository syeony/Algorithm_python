# 예전에 풀었던 SWEA 사이트의 1954번 문제 참고

n = int(input())
ask = int(input())

arr = [[0]*n for _ in range(n)]
    # 하,우,상,좌 달팽이 모양 순서대로 적어주기
dx = [1,0,-1,0]
dy = [0,1,0,-1]

s,e = 0,0
cnt = 0

for i in range(n*n,0,-1):
    arr[s][e]=i

    nx = s + dx[cnt]
    ny = e + dy[cnt]

    if nx>=n or ny>=n or nx<0 or ny<0 or arr[nx][ny]!=0:
        cnt=(cnt+1)%4
        nx = s+dx[cnt]
        ny = e+dy[cnt]
    
    s=nx
    e=ny
    
# for i in range(n):
#     print(" ".join(map(str,arr[i])))

x,y=0,0
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
        if arr[i][j]==ask:
            x,y=i,j
    print()

print(x+1,y+1)