T = int(input())
hakjum = ['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+']

for tc in range(1,T+1):
    n,k = map(int,input().split())
    score_arr = []
    k_score = 0

    for i in range(n):
        a,b,c = map(int, input().split())
        score = a*0.35+b*0.45+c*0.2
        score_arr.append(score)

    k_score = score_arr[k-1]
    same = len(score_arr)//10
    score_arr.sort() # 오름차순 정렬
    score_num = 0

    for i in range(n):
        if score_arr[i] == k_score:
            score_num = i
    
    j=0
    for i in range(n):
        if i==0:
            continue
        if i%same==0:
            j+=1
        if score_num==i:
            break

    print(f"#{tc} {hakjum[j]}")

    

    

