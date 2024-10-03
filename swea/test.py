# arr = [3,3,1,1,4]
# list = [0,2,0,2,1]

# for i in reversed(list):
#     if i == max(list):
#         print(list.index(i))
#         break

arr = [10,7,6]
print(arr[-1])
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])