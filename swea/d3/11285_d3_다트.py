import math

T = int(input())
p_arr = []

for tc in range(1,T+1):
    n = int(input())
    r = [20,40,60,80,100,120,140,160,180,200]
    p = 0

    for i in range(n):
        x, y = map(int,input().split())
        num = (x*x+y*y)**(1/2)

        for j in range(len(r)):
            if num <= r[j]:
                p+=10-j
                break
            else:
                p+=0
        # p += math.ceil(11-num/20)

    p_arr.append(f"#{tc} {p}")

for i in p_arr:
    print(i)
