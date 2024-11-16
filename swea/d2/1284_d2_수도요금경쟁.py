T = int(input())

def A(p,w):
    return p*w

def B(q,r,s,w):
    if w<=r:
        return q
    else:
        return q+s*(w-r)

for tc in range(1,T+1):
    p,q,r,s,w = map(int,input().split())

    if A(p,w) <= B(q,r,s,w):
        print(f"#{tc} {A(p,w)}")
    else:
        print(f"#{tc} {B(q,r,s,w)}")