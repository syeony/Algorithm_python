# 12931
# 모두 짝수면 //2
# 아니면 홀수 -1
# 반복

n = int(input())
arr = list(map(int,input().split()))
cnt = 0

while True:
  if sum(arr)==0:
    break

  flag = True
  for i in range(n):
    if arr[i]%2!=0:
      flag = False
      holsu=i
      break
  
  if flag:
    for i in range(n):
      arr[i]//=2
    cnt+=1
  else:
    arr[holsu]-=1
    cnt+=1

print(cnt)