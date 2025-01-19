while True:
    try:
        n,m = map(int,input().split())
        cnt=0
        for i in range(n,m+1):
            i=list(map(int,str(i)))
            if i.count(0)>1 or i.count(1)>1 or i.count(2)>1 or i.count(3)>1 or i.count(4)>1 or i.count(5)>1 or i.count(6)>1 or i.count(7)>1 or i.count(8)>1 or i.count(9)>1:
                continue
            else:
                cnt+=1
        print(cnt)
    except:
        break