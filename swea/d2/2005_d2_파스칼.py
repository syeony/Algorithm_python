T = int(input())

def piramid(arr):
    global n
    for i in range(n):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

    return 

for tc in range(1,T+1):
    n = int(input())
    arr = [[] for _ in range(n)]

    for i in range(n):
        x = i+1
        for j in range(x):
            arr[i].append(1)
    
    print(f"#{tc}")

    if len(arr) <= 2:
        piramid(arr)
    else:
        for i in range(2,n):
            for j in range(1,len(arr[i])-1):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        piramid(arr)
