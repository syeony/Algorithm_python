a,b = map(int,input().split())

list_a=list(map(int, input().split()))
list_b=list(map(int, input().split()))

list_a.extend(list_b)

list_a.sort()

for i in range(0,len(list_a)):
    print(list_a[i],end=' ')