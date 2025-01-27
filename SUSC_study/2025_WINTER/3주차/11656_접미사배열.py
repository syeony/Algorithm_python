n = list(input().strip())

arr=[]
for i in range(len(n)):
    arr.append("".join(n[i:len(n)]))

sorted_arr = sorted(arr)

for i in sorted_arr:
    print(i)