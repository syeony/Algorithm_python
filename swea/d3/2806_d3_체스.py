# 감을 못 잡겠어서 답지 참고
# 알고리즘 - 백트래킹

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    count = 0

    first_arr = []
    second_arr = []

    def filtering(): #대각선 거르는 함수
        position = len(first_arr)-1 #현재위치
        for i in range(position):
            if abs(first_arr[position]-first_arr[i]) == position-i: #현재열-이전열=현재행-이전행 같으면 대각선인거임
                return False
        return True

    def dfs(): #겹치는수 빼고 모든 경우의 수 구하는 함수
        if n == len(first_arr):
            mapping = ''.join(map(str, first_arr))
            second_arr.append(mapping)

        for i in range(n):
            if i not in first_arr:
                first_arr.append(i)
                if filtering(): #여기서 대각선 걸러줌
                    dfs() #재귀함수
                first_arr.pop() #백트래킹에 아주 중요한 녀석

    dfs()

    print(f"#{test_case} {len(second_arr)}")