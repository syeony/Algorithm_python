N = int(input())
l = list()

for i in range(0,N):
    l.append(i+1)

while True:
    if len(l)==1:
        break

    i=0
    while True:
        l[i]=0
        i+=2
        if i>=len(l):
            break

    l = [x for x in l if x!=0]

    

print(l[0])
    
