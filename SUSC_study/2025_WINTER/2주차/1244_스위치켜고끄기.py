n = int(input())
arr = list(map(int,input().split()))
t = int(input())

for i in range(t):
  a, b = map(int,input().split())
  
  if a==1: #남자
    for j in range(len(arr)):
      if (j+1)%b==0:
        if arr[j]==1:
          arr[j]=0
        elif arr[j]==0:
          arr[j]=1

  else: #여자
    if b==1:
      if arr[0]==1:
        arr[0]=0
      elif arr[0]==0:
        arr[0]=1
    else:
      if arr[b-1]==1:
        arr[b-1]=0
      elif arr[b-1]==0:
        arr[b-1]=1
      for j in range(1,b):
        if arr[b-1+j]==arr[b-1-j]:
          if arr[b-1+j]==1:
            arr[b-1+j]=0
            arr[b-1-j]=0
          elif arr[b-1+j]==0:
            arr[b-1+j]=1
            arr[b-1-j]=1
        else:
          break

print(" ".join(map(str,arr)))