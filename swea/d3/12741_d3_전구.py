# 시간초과떠서 배열에 담아뒀다가 한번에 출력해야함

T = int(input())

cnt_arr=[]

for tc in range(1,T+1):
    a,b,c,d = map(int,input().split())
    ab=[]
    cd=[]

    for i in range(a,b):
        ab.append(i)
    
    for i in range(c,d):
        cd.append(i)

    cnt = 0 
    if ab[0]>=cd[0]:
        for i in range(a,b):
            if i in cd:
                cnt += 1
    elif cd[0]>=ab[0]:
        for i in range(c,d):
            if i in ab:
                cnt += 1

    cnt_arr.append(cnt)

for i in range(len(cnt_arr)):   
    print(f"#{i+1} {cnt_arr[i]}")