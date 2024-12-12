# 실패

b = int(input())
cnt_arr = []

a=b
cnt = 0
while a>1:
    if a!=1:
        cnt+=1
    if a%3==0:
        a=a//3
    elif a%2==0:
        a=a//2
    else:
        a-=1
    # print('1:',a)
cnt_arr.append(cnt)

a=b
a-=1
cnt=1
while a>1:
    if a!=1:
        cnt+=1
    if a%3==0:
        a=a//3
    elif a%2==0:
        a=a//2
    else:
        a-=1
    # print('2:',a,cnt)
cnt_arr.append(cnt)

print(min(cnt_arr))