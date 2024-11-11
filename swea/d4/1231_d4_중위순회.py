# 답을 봄

def inorder(n):
    global word
    if n<=N: # word의 위치에 따라 전위, 중위, 후위
        inorder(n*2)
        word += arr[n-1][1]
        inorder(n*2+1)

for tc in range(1,11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    word = ''

    inorder(1)
    print(f"#{tc} {word}")