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

# arr=[]

# for _ in range(5):
#     row = list(map(int,input().split()))
#     arr.append(row)

# print(arr)

# arr = []
# arr.append([5,2])
# arr.append([7,4])
# arr.append([4,90])
# print(arr)
# print(len(arr))
# print(arr[0][0], arr[0][1], arr[-1][0], arr[-1][1])
# count = sum(row.count(4) for row in arr)
# print(count)

# from collections import deque

# x,y=1,1
# queue = deque()
# queue.append((x,y))
# print(x,y,queue)
# x,y=queue.popleft()
# print(x,y,queue)
# str = '0123'
# arr = [1,2,3]
# arr.insert(0,0)
# print(len(str), arr)
# arr = [1,2,5,6,6,5,7,3,3]
# i = 1  
# while i < len(arr):
#     if arr[i] == arr[i-1]:
#         del arr[i]
#         del arr[i-1]
#         i -= 1 
#     else:
#         i += 1 

# print(arr)

# num=11223344
# sorted_num = sorted(str(num))
# if list(str(num)) == sorted_num:
#     print(num)
# else:
#     print(num, sorted_num)

num = 12345

arr = list(map(int,str(num)))
print(arr)

def swap():
    temp = arr[0]
    arr[0] = arr[4]
    arr[4] = temp

swap()
print(arr)

print(int(''.join(map(str,arr))))