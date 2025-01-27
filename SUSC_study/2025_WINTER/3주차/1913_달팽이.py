n = int(input())
ask = int(input())

arr = [[0]*n for _ in range(n)]
    # 상,우,하,좌 달팽이 모양 순서대로 적어주기
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(n):
    for j in range(n):
        