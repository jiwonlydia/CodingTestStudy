# 큐에다가 노드를 넣는게 아니라 경로(path) 자체를 넣는다는게 포인트

import collections
all_paths = []
graph = [[1,2],[3],[3],[]]
# [[0,1,3],[0,2,3]]
n = len(graph)
path = [0]
queue = collections.deque()
# seen = set([0])
queue.append(path)

while queue:
    curr_path = queue.popleft()
    node = curr_path[-1] # path의 마지막 원소가 현재 노드
    print(curr_path)

    for next_node in graph[node]:
        temp_path = curr_path.copy()
        temp_path.append(next_node)
        if next_node == n - 1:
            all_paths.append(temp_path)
        else:
            queue.append(temp_path)

print(all_paths)