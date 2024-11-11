# 하다하다 안되서 답봄

T = int(input())

for tc in range(1,T+1):
    arr = list(input().strip())
    start = []
    end = []
    patern = 0

    if arr[0:10] == arr[-10:]:
        i = 0
        while True:
            start.append(arr[i])
            end.append(arr[-1])
            if len(start)>1 and start == end[::-1]:
                patern = len(start)
                break
    else:
        while True:
            arr.pop()
            if arr[0:10] == arr[-10:]:
                i = 0
                while True:
                    start.append(arr[i])
                    end.append(arr[-1])
                    if len(start)>1 and start == end[::-1]:
                        patern = len(start)
                        break

    print(f"#{tc} {patern}")