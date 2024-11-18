# 내 코드에서 잘못된 점을 gpt에게 물어봐서 고침

def solution(dirs):
    answer = 0
    dirs_dir = list(dirs.strip())
    x,y = 0,0
    visited = []
    
    for dir in dirs_dir:
        nx = x
        ny = y
        
        if dir == 'U':
            ny+=1
        elif dir == 'D':
            ny-=1
        elif dir == 'R':
            nx+=1
        elif dir == 'L':
            nx-=1
        
        if nx>5 or ny>5 or nx<-5 or ny<-5:
            continue
        
        if [x,y,nx,ny] not in visited and [nx,ny,x,y] not in visited:
            visited.append([x,y,nx,ny])
            visited.append([nx,ny,x,y])
            
        x = nx
        y = ny
            
    answer = len(visited)//2
    
    return answer