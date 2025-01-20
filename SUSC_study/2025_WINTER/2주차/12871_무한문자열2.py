s=input().strip()
t=input().strip()

a,b = min(s,t), max(s,t)
sub = len(b)-len(a)

a=a*sub

if a==b:
    print(1)
else:
    print(0)

