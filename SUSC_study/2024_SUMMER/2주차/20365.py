N=int(input())
arr=list(input())

first=arr[0]
count=1

for i in range(1,len(arr)):
    if arr[i]!=first and arr[i]!=arr[i-1]:
        count+=1

print(count)