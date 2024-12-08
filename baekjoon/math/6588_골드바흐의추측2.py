import sys

sosu = [True] * 1000001 # 처음엔 모든 수가 전부 소수라고 가정
sosu[0],sosu[1]=False,False # 0,1은 제외

for i in range(2,1000001):
    if i*i > 1000000: break
    if sosu[i] == False: continue
    for j in range(i*i,1000001,i): # 2-> 4,6,8,10,...제외 (2로 나눠지니까 소수가 아님)
        sosu[j] = False

while True:
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        break
    for i in range(3,num,2):
        if sosu[i] == True and sosu[num-i] == True:
            print(f"{num} = {i} + {num-i}")
            break
        else:
            continue
    else:
        print("Goldbach's conjecture is wrong.")
