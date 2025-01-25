n = int(input())
arr = list(map(int,input().split()))
first_index = 0
first_num = 0
cnt = 0

while sum(arr)>0:
    for i in range(n):
        if arr[i]==0:
            continue
        else:
            first_index = i
            first_num = arr[i]
            break
    
    for i in range(first_index,n):
        if arr[i]==0:
            first_num-=1
            continue
        
        if arr[i]==first_num:
            arr[i]=0
            first_num-=1
    
    cnt += 1

print(cnt)
        
