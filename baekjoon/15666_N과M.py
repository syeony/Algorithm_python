n,m=map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
num = []
result = []

def solution(num):
    global arr,result
    if len(num) == m:
        result.append(num)
    
    for i in arr:
        num.append(i)
        solution(num)
        num.pop()

solution(num)
result = list(set(result))

print(result)