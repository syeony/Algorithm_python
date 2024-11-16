T = int(input())

for tc in range(1,T+1):
    n = int(input())
    week = list(map(int, input().split()))
    study_day = 0
    day = 0

    while True:
        if week.index(1)>=1:
            del week[0]
            week.append(0)
        else:
            break

    print(week)
    
    flag = False
    while True:
        for i in range(7):
            day += 1
            if week[i] == 1:
                study_day += 1
            if study_day >= n:
                flag = True
                break
        if flag:
            break

    print(f"#{tc} {day}")