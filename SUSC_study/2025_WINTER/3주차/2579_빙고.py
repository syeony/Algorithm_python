n=5
arr1 = [list(map(int,input().split(" "))) for _ in range(n)]
arr2 = [list(map(int,input().split(" "))) for _ in range(n)]

# arr2를 일차원배열로 만들어버리기
arr3 = []
for i in range(n):
    for j in range(n):
        arr3.append(arr2[i][j])

cnt=0
def check(i,j):
    # 구현

while(cnt<3):
    index=0
    flag=False
    for i in range(n):
        for j in range(n):
            if arr1[i][j]==arr3[index]:
                arr1[i][j]=0
                cnt = check(i,j)
                index+=1
                flag=True
                break
        if flag:
            break