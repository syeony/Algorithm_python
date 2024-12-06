a=input()
arr=[]
b=''
cnt = 1
flag = False
for i in a:
    if i == '<':
        b+=i
        flag = True
    elif flag and i != '>':
        b+=i
    elif i == '>':
        b+=i
        arr.append(b)
        b=''
        flag = False
    else:
        if i == ' ':
            pass
        elif cnt<len(a) and (a[cnt] == ' ' or a[cnt] == '<' or cnt==len(a)-1):
            if a[cnt] == '<':
                b+=i
                arr.append(b[::-1])
                b=''
            if a[cnt]==' ':
                b+=i
                arr.append(b[::-1])
                b=''
                arr.append(' ')
            if cnt==len(a)-1:
                b+=i
                b+=a[-1]
                arr.append(b[::-1])
                b=''
        else:
            b+=i
    cnt+=1

print(''.join(arr))
