a=list(input().strip())

for i in a:
  if i.islower():
    print(i.upper(),end='')
  else:
    print(i.lower(),end='')

# print(input().swapcase())