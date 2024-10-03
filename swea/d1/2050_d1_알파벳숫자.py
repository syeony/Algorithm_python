# ord(), chr() -> 아스키코드 변환

T = input()
arr = list(T)

for i in arr:
    num = ord(i) - 64
    print(num, end=' ')
