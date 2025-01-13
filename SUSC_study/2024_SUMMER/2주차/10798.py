arr=[]
for i in range(5):
	arr.append(list(input()))

new_arr = [[None for _ in range(15)] for _ in range(15)]

for i in range(0,len(arr)):
	for j in range(0,len(arr[i])):
		new_arr[j][i]=arr[i][j]

for i in range(0,len(new_arr)):
	for j in range(0,len(new_arr[i])):
		if new_arr[i][j] == None:
			pass
		else:
		    print(new_arr[i][j],end="")