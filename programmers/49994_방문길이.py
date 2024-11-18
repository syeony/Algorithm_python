# 너무 복잡하고 무언가 단단히 잘못되었음...

def solution(dirs):
    answer = 0
    dirs_dir = list(dirs.strip())
    x,y = 0,0
    arr = [[] for _ in range(len(dirs_dir))]
    arr2 = []
    
    for i in range(len(dirs_dir)):
        if dirs_dir[i] == 'U':
            y+=1
            if x>5 or y>5 or x<-5 or y<-5:
                y-=1
            else:
                arr[i].append([x,y-1])
                arr[i].append([x,y])
        elif dirs_dir[i] == 'L':
            x-=1
            if x>5 or y>5 or x<-5 or y<-5:
                pass
            else:
                arr[i].append([x+1,y])
                arr[i].append([x,y])
        elif dirs_dir[i] == 'R':
            x+=1
            if x>5 or y>5 or x<-5 or y<-5:
                pass
            else:
                arr[i].append([x-1,y])
                arr[i].append([x,y])
        elif dirs_dir[i] == 'D':
            y-=1
            if x>5 or y>5 or x<-5 or y<-5:
                pass
            else:
                arr[i].append([x,y+1])
                arr[i].append([x,y])
        
    for i in range(len(arr)):
        first = arr[i][0]+arr[i][1]
        second = arr[i][1]+arr[i][0]
        if (first or second) in arr2:
            pass
        else:
            arr2.append(first)
            arr2.append(second)
    
    answer = len(arr2)//2
    
    return answer