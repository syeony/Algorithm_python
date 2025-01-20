s=list(input().strip())
t=list(input().strip())

a,b = min(s,t), max(s,t)
a = "".join(a)
answer = 1

for i in range(0,len(b),len(a)):
  if a=="".join(b[i:i+len(a)]):
    continue
  else:
    answer = 0
    break

print(answer)