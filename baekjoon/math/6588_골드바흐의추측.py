def sosu(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    else:
        return True

arr = []

while True:
    num = int(input())
    if num == 0:
        break
    first,second = 0,0
    for i in range(3,num):
        if i % 2 != 0 and sosu(i) == True and (num-i) % 2 != 0 and sosu(num-i) == True:
            first = i
            second = num-i
            arr.append(f"{num} = {first} + {second}")
            break
        else:
            continue
    else:
        arr.append("Goldbach's conjecture is wrong.")

for i in arr:
    print(i)