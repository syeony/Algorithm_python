# 진짜 모르겠어서 답 봄
# 참고 블로그: https://define-me.tistory.com/85
# gpt한테도 계속 물어봄

n = int(input())
result=''

if n == 0:
    print(0)
    exit # 걍 밑으로 안감 여기서 끝!

while n!=0:
    if n%-2 != 0: # -2로 나누어 떨어지지 않으면 나머지+2, 몫+1 해줘야함
        temp=str(n%(-2)+2)
        result+=temp
        n = n//-2+1
    else:
        temp=str(n%(-2))
        result+=temp
        n = n//-2

print(result[::-1])