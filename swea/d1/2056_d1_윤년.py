T = int(input())

for test_case in range(1, T + 1):
    calendar = int(input())
    calendar_arr = list(map(int, str(calendar)))

    year = calendar // 10000
    month = (calendar % 10000)//100 # 몫 int형으로 구할땐 // 사용
    day = calendar % 100

    if month < 1 or month > 12:
        print(f"#{test_case} -1")
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day < 1 or day > 31):
        print(f"#{test_case} -1")
    elif month == 4 or month == 6 or month == 9 or month == 11 and (day < 1 or day > 30):
        print(f"#{test_case} -1")
    elif month == 2 and (day < 1 or day > 28):
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case}",end=' ')
        for i in calendar_arr[0:4]:
            print(i, end='')
        print("/", end='')
        for i in calendar_arr[4:6]:
            print(i, end='')
        print("/", end='')
        for i in calendar_arr[6:8]:
            print(i, end='')
        print("")