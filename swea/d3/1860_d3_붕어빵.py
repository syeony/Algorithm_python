# 처음식으로 하니까 테스트케이스 770개만 통과되서 지피티 사용해서 식 세움

T = int(input())

for test_case in range(1, T+1):
    n,m,k = map(int,input().split()) # n:사람수 m:시간 k:붕어빵
    n_arr = list(map(int,input().split()))
    n_arr = sorted(n_arr)

    result = "Possible" #기본값

    for i in range(n): # 붕어빵 개수가 현재 사람 수보다 적으면 = 임파서블
        if (n_arr[i]//m)*k < i+1: # 처음 식 = n_arr[i] < m_count or i+1 < k_count
            result = "Impossible"
            break

    print(f"#{test_case} {result}")
