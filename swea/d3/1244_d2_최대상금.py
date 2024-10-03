T1 = int(input())

for test_case in range(1, T1 + 1):
    a, b = map(int,input().split())
    arr = list(map(int, str(a)))

    max_value = max(arr)
    for i in range(b):
        for back in range(len(arr)-1,-1,-1):
            if max_value == 