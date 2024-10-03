arr=list(input())
new_arr=[]

# for i in range(len(arr)-1,0,-1):
#    arr2=list(reversed(arr))
#    if arr==arr2:
#       break
#    else:
#       arr.append(arr[i-1])
#       print(i-1, arr[i-1])

if arr!=list(reversed(arr)):
    for i in range(0,len(arr)):
        new_arr.append(arr[i])
        arr2=arr+list(reversed(new_arr))
        if arr2==list(reversed(arr2)):
            break

print(len(arr+new_arr))