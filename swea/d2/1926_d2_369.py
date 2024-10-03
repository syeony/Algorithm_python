num = int(input())

for i in range(1, num+1):
    new = str(i)
    new = new.replace('3','-')
    new = new.replace('6','-')
    new = new.replace('9','-')

    count = new.count('-')

    if count == 1:
        print("-", end=' ')
    elif count > 1:
        print("-"*count, end=' ')
    else:
        print(new, end=' ')
