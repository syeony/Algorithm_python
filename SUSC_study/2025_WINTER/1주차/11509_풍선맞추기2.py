n = int(input())
arr = list(map(int,input().split()))
first_index = 0
first_num = 0
cnt = 0

while max(arr)>0:
    first_index = arr.index(max(arr))
    first_num = arr[first_index]
    
    for i in range(first_index,n):       
        if arr[i]==first_num:
            arr[i]=0

        first_num-=1
    
    cnt += 1

print(cnt)
        
