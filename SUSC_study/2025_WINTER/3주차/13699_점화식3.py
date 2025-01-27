# 풀고나서 다른 풀이 구글링으로 찾아본 것

n = int(input())
arr=[0]*36
arr[0]=1
arr[1]=1

for i in range(2,n+1):
    for j in range(i):
        arr[i] += arr[j]*arr[i-j-1]

print(arr[n])