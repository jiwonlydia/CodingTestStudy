# 미로 탈출
N = 5 ; M = 6
graph = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque

def bfs(graph, x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: # 범위 밖에 존재한다면 무시
                continue # 여기에 걸리면 아래 모든 if문 무시하고 while문 처음으로 돌아감
            if graph[nx][ny] == 0: # 괴물 존재하면 무시
                continue
            if graph[nx][ny] == 1: # 처음 방문이면
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(graph, 0, 0))
















# 나의 맨 처음 풀이
# visited = [[0]*M for _ in range(N)]
# visited[0][0] = 1
# def bfs(graph, i, j) :
#     q = deque()
#     q.append((i, j))
#     count = 1
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0<=nx<N and 0<=ny<M: # 범위 내에 있으면
#                 if visited[nx][ny] == 0 and graph[nx][ny] == 1 : # 아직 방문 안했고 괴물이 없으면
#                     q.append((nx, ny))
#                     visited[nx][ny] = 1
#                     count += 1
#                     print('(N,M)=',(nx,ny))
#                     if nx == N-1 and ny == M-1 : # 출구에 도착하면
#                         return count
#
# print(bfs(graph, 0, 0))

###################################################################################################

# 모범답안
from collections import deque

# N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상,하,좌,우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# # BFS 소스코드 구현
# def bfs(x, y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque()
#     queue.append((x, y))
#
#     # 큐가 빌 때까지 반복
#     while queue:
#         x, y = queue.popleft()
#
#         # 현재 위치에서 네 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             # 미로찾기 공간을 벗어난 경우 무시
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n - 1][m - 1]
#
# print(bfs(0,0))
