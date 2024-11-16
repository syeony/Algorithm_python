N=int(input())
newN=N
count=0

if N>=5:
    while newN>0 and count!=-1:
        if newN>=5:
            count+=1
            newN-=5
        elif newN==3:
            count+=1
            newN-=3
        elif N>5 and (newN==4 or newN==1):
            newN+=5
            count-=1
            if newN%3==0:
                while newN>0:
                    newN-=3
                    count+=1
            else:
                count=-1
        elif N>10 and newN==2: #12
            newN+=10
            count-=2
            if newN%3==0:
                while newN>0:
                    newN-=3
                    count+=1
            else:
                count=-1
        else:
            count=-1
elif N==4:
    count=-1
elif N==3:
    count+=1

print(count)