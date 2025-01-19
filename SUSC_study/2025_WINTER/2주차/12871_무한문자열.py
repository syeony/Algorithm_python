s=list(input().strip())
t=list(input().strip())

a,b = min(s,t), max(s,t)
a = "".join(a)
answer = 1

while True:
    if len(b)==0:
        break
    i=0
    if a=="".join(b[i:i+len(a)]):
        b[i:i+len(a)]='0'
        b.pop(0)
    else:
        answer = 0
        break

print(answer)