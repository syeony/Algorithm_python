#실패

from collections import deque

T = int(input())  # 테스트 케이스 수

results = []
for tc in range(1, T + 1):
    n = int(input())  # 수영장 크기
    arr = [list(map(int, input().split())) for _ in range(n)]  # 수영장 지도

    # 시작 위치 및 도착 위치 입력
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    # 방향 벡터 (상하좌우)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # BFS를 위한 큐
    q = deque([(start_x, start_y, 0)])  # (x, y, time)
    visited = [[False] * n for _ in range(n)]

    visited[start_x][start_y] = True

    # BFS 탐색 시작
    def bfs():
        while q:
            x, y, time = q.popleft()

            # 도착점에 도달하면 시간 반환
            if (x, y) == (end_x, end_y):
                return time

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                # 경계 조건
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                # 장애물(1)은 지나갈 수 없음
                if arr[nx][ny] == 1:
                    continue

                # 소용돌이 처리
                if arr[nx][ny] == 2 and (time + 1) % 3 != 2:
                    continue

                # 이미 방문한 경우
                if visited[nx][ny]:
                    continue

                # 방문 표시 및 큐 추가
                visited[nx][ny] = True
                q.append((nx, ny, time + 1))

    # BFS 수행
    result = bfs()
    results.append(f"#{tc} {result}")

# 결과 출력
print("\n".join(results))


