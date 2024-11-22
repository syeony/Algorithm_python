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

# num = 12345

# arr = list(map(int,str(num)))
# print(arr)

# def swap():
#     temp = arr[0]
#     arr[0] = arr[4]
#     arr[4] = temp

# swap()
# print(arr)

# print(int(''.join(map(str,arr))))

# arr = [1,2,3]
# num = int(str(arr[0])+str(arr[1]))
# print(num)
# print(sorted(arr))
# n=5
# arr=[]
# while len(arr) < n:
#     # 공백 또는 줄바꿈으로 입력된 숫자를 추가
#     arr.extend(map(int, input().split()))
# print(arr)

# arr=[1,2,3]
# two = ''

# two += str(arr[0])
# two += str(arr[1])

# print(int(two))

# arr = [1,2]
# arr[0] = str(arr[0]).replace('1','ONE')
# print(arr)


# q = [2,4]
# num = q.pop(0) #선입선출
# print(num)

# arr=['a','b','c','d']
# print(arr[0:2])
# print(arr[-2:])

# n = 3.5
# print(round(n))

# n = 'aa'
# if '*' not in n:
#     print('True')
# else:
#     print('False')

# arr = [[1,1,2,3],[1,2,3,4]]
# sum = 0
# for i in range(len(arr)):
#     sum += arr[i].count(1)

# print(sum)

# arr=[8,4,1,9]
# arr.sort()
# print(arr)
# for i in range(0,len(arr),2):
#     arr[i]=0

# print(arr)

# def name(word):
#     if not word[0].isupper():
#         return False
    
#     for i in word[1:]:
#         if not i.islower():
#             return False
#     return True

# word = 'Tsd543'

# if name(word):
#     print(1)
# else:
#     print(2)

# arr = ['#','.','#']
# print(arr.count('#'))

# arr = [[1,1,2],[2,3]]
# li = list(set(arr[0]))
# print(len(li))

# import math
# print(math.ceil(3.14))

# hi = 'hi'.replace('h','0')
# print(hi)

# num = 'hi'
# print(num.isdigit()) # True

# arr = [1,2,3]
# print(arr.index(2))
# del arr[1]
# print(arr)

# import math
# L = math.sqrt((0-0)**2+(100-0)**2)

# cost = 1.0 * (L**2)
# print(round(cost))

# arr = [1,2,3]
# del arr[2]
# print(arr)

# print(7//-2, 7%-2)

# result='1010'
# print(result[::-1])

# a = 'D 2'
# print(a[2])

# b=[[1,2]]
# x,y=b.pop()
# print(x,y)

a=['a']*7

a[1] = 'b'
print(a)