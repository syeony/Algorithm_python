def solution(nums):
    answer = 0
    available = len(nums)//2
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
            
    if len(arr)>available:
        answer = available
    else:
        answer = len(arr)
        
    return answer