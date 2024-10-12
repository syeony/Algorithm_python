# arr = [3,3,1,1,4]
# list = [0,2,0,2,1]

# for i in reversed(list):
#     if i == max(list):
#         print(list.index(i))
#         break

# arr = [10,7,6]
# print(arr[-1])
# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i])

# arr = sorted(arr)
# print(arr)

# arr = [list(input().split()) for _ in range(5)]
# arr_sorted = sorted(arr, key=lambda x: x[0], reverse=True)
# print(arr_sorted)

# arr = [1,2,3,4,5]
# arr.append(arr[0])
# del(arr[0])
# print(arr)

# arr = [[1,2],3]
# if [1,2] not in arr:
#     arr.append(4)
# print(arr)

arr=[]

for _ in range(5):
    row = list(map(int,input().split()))
    arr.append(row)

print(arr)