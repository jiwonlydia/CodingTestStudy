places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

result = [1,0,1,1,1]
place = places[0] # 첫번째 대기실

from collections import deque

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(place, i, j):
    visited = [[0]*5 for _ in places]
    q = deque()
    q.append((i,j,0))
    while q:
        x, y, dist = q.popleft()
        if dist<=2 and place[x][y]=='P': # 거리두기 지키지 않음
            return False
        if dist > 2: # 거리두기 지킴
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            nd = dist + 1
            if 0 <= nx <= 4 and 0 <= ny <= 4:
                if place[nx][ny] != 'X' and visited[nx][ny] == 0:
                    q.append((nx,ny,nd))
                    visited[nx][ny] = 1
    return True

def solution(places):
    answer = []
    for place in places:
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P':
                    if not bfs(place, i, j):
                        answer.append(0)
        else:
            answer.append(1)
    return answer
















#######################################################################

# from collections import deque
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]  # 상하좌우
#
#
# def bfs(place, i, j):
#     visit = [[0] * 5 for _ in range(5)]
#     q = deque()
#     q.append((i, j, 0))
#     visit[i][j] = 1
#     while q:
#         x, y, dist = q.popleft()
#         if 0 < dist < 3 and place[x][y] == 'P':
#             return False
#         if dist > 2:
#             break  # 거리가 3부터는 탐색 중단(거리두기를 잘 지킨 경우이기 때문에)
#         for k in range(4):
#             nx, ny, nd = x + dx[k], y + dy[k], dist + 1
#             if 0 <= nx < 5 and 0 <= ny < 5:
#                 if place[nx][ny] != 'X' and not visit[nx][ny]:  # 파티션이 있는 경우만 아니면 이동가능
#                     q.append((nx, ny, nd))
#                     visit[nx][ny] = 1
#     return True
#
#
# def solution(places):
#     answer = []
#     for place in places:
#         chk = 0
#         for i in range(len(place)):
#             for j in range(len(place[0])):
#                 if place[i][j] == "P":
#                     if not bfs(place, i, j):
#                         answer.append(0)
#                         chk = 1
#                         break
#             if chk:
#                 break
#         else:
#             answer.append(1)
#
#     return answer
