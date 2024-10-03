import sys
sys.stdin = open("/Users/ohseungyeon/Documents/swea/d3/1208_input.txt", "r")

for test_case in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))

    for _ in range(N):
        i=arr.index(max(arr))
        j=arr.index(min(arr))
        arr[i] = arr[i]-1
        arr[j] = arr[j]+1


    result = max(arr)-min(arr)
    print(f"#{test_case} {result}")