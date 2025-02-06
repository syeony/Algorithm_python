n=5
arr1 = [list(map(int,input().split(" "))) for _ in range(n)]
arr2 = [list(map(int,input().split(" "))) for _ in range(n)]

# arr2를 일차원배열로 만들어버리기
arr3 = []
for i in range(n):
    for j in range(n):
        arr3.append(arr2[i][j])

result = 0
index=0
cnt=0

def check():
    global cnt
    cnt=0

    # 구현
    for i in range(n):
        if all(arr1[i][j]==0 for j in range(n)):
            cnt+=1
    
    for j in range(n):
        if all(arr1[i][j]==0 for i in range(n)):
            cnt+=1

    if all(arr1[i][i]==0 for i in range(n)):
        cnt+=1

    if all(arr1[i][n-i-1]==0 for i in range(n)):
        cnt+=1


while(index < len(arr3)):
    flag=False

    for i in range(n):
        for j in range(n):
            if arr1[i][j]==arr3[index]:
                # print(arr3[index])
                arr1[i][j]=0
                check()
                if cnt==3:
                    result=index+1
                    flag=True
                    index+=1
                    break
        if flag:
            break
    if flag:
        break

print(result)