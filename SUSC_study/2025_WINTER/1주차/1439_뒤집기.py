import math

n = list(input().strip())
start=n[0]
cnt=0

for i in range(len(n)):
  if start==n[i]:
    continue
  else:
    cnt+=1
    start=n[i]

# ceil은 무조건 위로 올려주는거 예) 1.1->2
print(math.ceil(cnt/2))