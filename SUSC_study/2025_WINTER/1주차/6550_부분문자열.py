while True:
  try:
    a,b = input().split()
    a = list(a)
    b = list(b)

    cnt = len(a)
    j=0
    for i in range(len(b)):
      if len(a)==0:
        break
      else:
        if b[i]==a[j]:
          a.pop(0)
        else:
          continue

    if len(a)==0:
      print('Yes')
    else:
      print('No')
  except:
    break