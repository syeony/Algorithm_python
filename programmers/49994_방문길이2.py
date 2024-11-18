# 내 코드에서 잘못된 점을 gpt에게 물어봄
# 두 좌표를 배열이 아닌 튜플로 저장함

def solution(dirs):
    answer = 0
    dirs_dir = list(dirs.strip())
    x,y = 0,0
    visited = set()
    
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
        
        if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            
        x = nx
        y = ny
    
    answer = len(visited)//2
    
    return answer