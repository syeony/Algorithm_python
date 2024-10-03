a,b=map(int,input().split())

start, end, count = 0, 0, 0

arr=list(map(int,input().split()))

# while start<a and end<a:
#     if arr[start]+arr[end] <= b:
#         if end==a-1:
#             start+=1
#         if arr[start]+arr[end] == b:
#             count+=1
#             print(arr[start], arr[end], end='/')
#         end+=1
#     elif arr[start]+arr[end] > b:
#         if arr[end]>=b:
#             end+=1
#         else:
#             start+=1

while start<a and end<a:
    if arr[end]==a-1:
        start+=1
    if arr[start]==a-1:
        end+=1

    if arr[start]+arr[end]<b:
        end+=1
    elif arr[start]+arr[end]==b:
        count+=1
        end+=1
    else:
        if arr[end]>=b:
            end+=1
        start+=1

print(count)
