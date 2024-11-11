T = int(input())

for test_case in range(1,T+1):
    testcase, N = input().split()
    arr = list(input().split())
    
    for i in range(len(arr)):
        if arr[i] == 'ZRO':
            arr[i] = int(arr[i].replace('ZRO','0'))
        elif arr[i] == 'ONE':
            arr[i] = int(arr[i].replace('ONE','1'))
        elif arr[i] == 'TWO':
            arr[i] = int(arr[i].replace('TWO','2'))
        elif arr[i] == 'THR':
            arr[i] = int(arr[i].replace('THR','3'))
        elif arr[i] == 'FOR':
            arr[i] = int(arr[i].replace('FOR','4'))
        elif arr[i] == 'FIV':
            arr[i] = int(arr[i].replace('FIV','5'))
        elif arr[i] == 'SIX':
            arr[i] = int(arr[i].replace('SIX','6'))
        elif arr[i] == 'SVN':
            arr[i] = int(arr[i].replace('SVN','7'))
        elif arr[i] == 'EGT':
            arr[i] = int(arr[i].replace('EGT','8'))
        elif arr[i] == 'NIN':
            arr[i] = int(arr[i].replace('NIN','9'))

    arr = sorted(arr)
    
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = str(arr[i]).replace('0','ZRO')
        elif arr[i] == 1:
            arr[i] = str(arr[i]).replace('1','ONE')
        elif arr[i] == 2:
            arr[i] = str(arr[i]).replace('2','TWO')
        elif arr[i] == 3:
            arr[i] = str(arr[i]).replace('3','THR')
        elif arr[i] == 4:
            arr[i] = str(arr[i]).replace('4','FOR')
        elif arr[i] == 5:
            arr[i] = str(arr[i]).replace('5','FIV')
        elif arr[i] == 6:
            arr[i] = str(arr[i]).replace('6','SIX')
        elif arr[i] == 7:
            arr[i] = str(arr[i]).replace('7','SVN')
        elif arr[i] == 8:
            arr[i] = str(arr[i]).replace('8','EGT')
        elif arr[i] == 9:
            arr[i] = str(arr[i]).replace('9','NIN')

    print(f"{testcase}")
    for i in range(len(arr)):
        print(f"{arr[i]}",end=' ')