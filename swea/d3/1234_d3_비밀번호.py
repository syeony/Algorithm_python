# for문으로 앞뒤같은숫자 검사했더니 인덱스에러나서 while문으로 바꿈
# 마지막 테케가 자꾸 막혀서 알아보니 m으로 입력받을때 맨앞의 0이 리스트에 안들어가는 문제발견
# m길이와 arr길이가 다르면 arr맨앞에 0 다시 추가해주는 조건 추가

for test_case in range(1,11):
    n, m = input().split()
    temp = len(m)
    arr = list(map(int, str(m)))

    if temp != len(arr):
        arr.insert(0,0)

    i = 1
    while i<len(arr):
        if arr[i] == arr[i-1]:
            del arr[i]
            del arr[i-1]
            i -= 1
        else:
            i += 1
    
    print(f"#{test_case} {''.join(map(str, arr))}")