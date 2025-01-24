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
        k=b-1
        for j in range(len(arr)):
            if (k-j>=0 and k+j<n) and arr[k-j]==arr[k+j]:
                if arr[k-j]==1:
                    arr[k-j]=0
                    arr[k+j]=0
                elif arr[k-j]==0:
                    arr[k-j]=1
                    arr[k+j]=1
            else:
                break
        
# 아 출력 조건 못봤어 하...
# print(" ".join(map(str,arr)))

for i in range(0,len(arr),20):
    print(" ".join(map(str, arr[i:i+20])))
          