# gpt 도움받음
# 접근법: e에서 s로 바꿔나가기

T = int(input())

for tc in range(1,T+1):
    s = input().strip()
    e = input().strip()

    def a(s,e):
        while len(e)>len(s):
            if e[-1]=='X':
                e = e[:-1]
            elif e[-1]=='Y':
                e = e[:-1]
                e = e[::-1]

        if e==s:
            return 'Yes'
        else:
            return 'No'
    
    print(f"#{tc} {a(s,e)}")