# 음료수 얼려먹기 - 내 풀이 : BFS로 품
# N = 4 ; M = 5
# graph = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]
N = 15 ; M = 14
graph = [[0,0,0,0,0,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,1,1,1,1,1,1,0],
[1,1,0,1,1,1,0,1,1,0,1,1,1,0],
[1,1,0,1,1,1,0,1,1,0,0,0,0,0],
[1,1,0,1,1,1,1,1,1,1,1,1,1,1],
[1,1,0,1,1,1,1,1,1,1,1,1,0,0],
[1,1,0,0,0,0,0,0,0,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,1,1,1,0,0,1,1],
[1,1,1,0,0,0,1,1,1,1,1,1,1,1],
[1,1,1,0,0,0,1,1,1,1,1,1,1,1]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
from collections import deque
visited = [[0]*M for _ in range(N)] # 방문 여부 체크를 위한 리스트
def bfs(graph, i, j): # (i,j)는 시작 지점
    q = deque()
    q.append((i, j)) # 시작 지점 먼저 큐에 추가
    visited[i][j] = 1
    size = 1
    while q:
        x, y = q.popleft()  # 탐색할 좌표
        # print('x:', x, ' y:', y)
        for k in range(4): # 상하좌우로 이동
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M: # 범위 안에 있고
                if graph[nx][ny] == 0 and visited[nx][ny] == 0: # 얼음틀이 비어있고 아직 방문 안했으면
                    # print('(nx,ny)',(nx,ny))
                    size += 1
                    q.append((nx, ny)) # 다음 탐색 후보로 추가
                    visited[nx][ny] = 1 # 방문처리
    print('size : ', size)
    return True

def solution(graph):
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and visited[i][j] == 0 : # 0인 곳을 찾아서 탐색 시작
                # print('start bfs i, j = ',(i,j))
                if bfs(graph, i, j):
                    count += 1
    print(count)
    return count

solution(graph)

######################################################################################
# 교재 모범답안: DFS 사용

# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
#
# # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
# def dfs(x, y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#
#         return True
#     return
#
# # 모든 노드(위치)에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i,j) == True:
#             result += 1
# print(result)




