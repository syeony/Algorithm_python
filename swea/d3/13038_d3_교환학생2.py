# 모든 시작일수 다 고려하여야 함

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    week = list(map(int, input().split()))
    day_arr = []

    week1 = week[1:]
    week1.append(week[0])
    week2 = week1[1:]
    week2.append(week1[0])
    week3 = week2[1:]
    week3.append(week2[0])
    week4 = week3[1:]
    week4.append(week3[0])
    week5 = week4[1:]
    week5.append(week4[0])
    week6 = week5[1:]
    week6.append(week5[0])
    
    day = 0
    study_day = 0
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
    day_arr.append(day)

    day = 0
    study_day = 0
    flag = False
    while True:
        for i in range(7):
            day += 1
            if week1[i] == 1:
                study_day += 1
            if study_day >= n:
                flag = True
                break
        if flag:
            break
    day_arr.append(day)

    day = 0
    study_day = 0
    flag = False
    while True:
        for i in range(7):
            day += 1
            if week2[i] == 1:
                study_day += 1
            if study_day >= n:
                flag = True
                break
        if flag:
            break
    day_arr.append(day)

    day = 0
    study_day = 0
    flag = False
    while True:
        for i in range(7):
            day += 1
            if week3[i] == 1:
                study_day += 1
            if study_day >= n:
                flag = True
                break
        if flag:
            break
    day_arr.append(day)

    day = 0
    study_day = 0
    flag = False
    while True:
        for i in range(7):
            day += 1
            if week4[i] == 1:
                study_day += 1
            if study_day >= n:
                flag = True
                break
        if flag:
            break
    day_arr.append(day)

    day = 0
    study_day = 0
    flag = False
    while True:
        for i in range(7):
            day += 1
            if week5[i] == 1:
                study_day += 1
            if study_day >= n:
                flag = True
                break
        if flag:
            break
    day_arr.append(day)

    day = 0
    study_day = 0
    flag = False
    while True:
        for i in range(7):
            day += 1
            if week6[i] == 1:
                study_day += 1
            if study_day >= n:
                flag = True
                break
        if flag:
            break
    day_arr.append(day)

    print(f"#{tc} {min(day_arr)}")