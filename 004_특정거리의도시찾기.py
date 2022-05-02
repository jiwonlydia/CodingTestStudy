# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기
# n = 4 ; m = 4 ; k = 2 ;  x = 1
# graph = [[], [2, 3], [3, 4], [], []]

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

from collections import deque

distance = [-1] * (n+1)
distance[x] = 0
q = deque()
q.append(x)

while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1: # 아직 방문하지 않은 도시라면
            distance[next] = distance[now] + 1
            q.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

###########################################################################
# 모범 답안
# from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
# n, m, k, x = map(int, input().split())

# graph = [[] for _ in range(n + 1)]
#
# # 모든 도로 정보 입력받기 (그래프를 인접리스트 형태로 만드는 코드!! 중요)
# # 그래프에서 첫번째 원소는 인덱스 => graph[a]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# print(graph)
# 모든 도시에 대한 최단거리 초기화
# distance = [-1] * (n + 1) # 왜 n개가 아니라 (n+1)개?
# distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정


# 너비 우선 탐색(BFS) 수행
#
# q = deque([x])
# while q:
#     now = q.popleft()
#     # 현재 도시에서 이동할 수 있는 모든 도시를 확인
#     for next_node in graph[now]:
#         # 아직 방문하지 않은 도시라면
#         if distance[next_node] == -1:
#             # 최단 거리 갱신
#             distance[next_node] = distance[now] + 1
#             q.append(next_node)

# # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
# check = False
# for i in range(1, n + 1):
#     if distance[i] == k:
#         print(i)
#         check = True

# 만약 최단거리가 K인 도시가 없다면, -1 출력
# if check == False:
#     print(-1)
