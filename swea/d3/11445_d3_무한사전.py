# input().strip()로 받아야 함
# input()으로만 받고 +'a' 하면 input() 앞뒤에 공백이 생겨서 ' man a' 이렇게 되버림

T = int(input())

for tc in range(1,T+1):
    p = input().strip() # input() => ' man a'
    q = input().strip() # input().strip() => 'mana'
    same = p+'a'
    result = 'Y'

    if q == same:
        result = 'N'

    print(f"#{tc} {result}")