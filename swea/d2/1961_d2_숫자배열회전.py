T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    arr1 = list(zip(*arr[::-1]))
    arr2 = list(zip(*arr1[::-1]))
    arr3 = list(zip(*arr2[::-1]))

    print(f"#{tc}")

    for i in range(n): # 숫자배열을 join할때는 문자열로 변경하여 join해야한다
        print("".join(map(str,arr1[i])),end=' ')
        print("".join(map(str,arr2[i])),end=' ')
        print("".join(map(str,arr3[i])),end=' ')
        print()
