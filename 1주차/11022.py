N=int(input())

for i in range(0,N):
    a, b = map(int,input().split())
    j=i+1
    print("Case #",end='')
    print(j,end='')
    print(":",a,"+",b,"=",a+b)