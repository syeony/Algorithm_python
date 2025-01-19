arr = list(input().strip())
n = input()
cnt=0

for i in range(len(arr)):
    if "".join(arr[i:i+len(n)])==n:
        cnt+=1
        arr[i:i+len(n)]='0'

print(cnt)