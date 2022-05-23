# 백준 1260: DFS와 BFS
# https://www.acmicpc.net/problem/1260

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# n = 4 ; m = 5 ; v = 1
# graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

# DFS
path = [v]
seen = set([v])

def dfs(node):
    for neighbor in sorted(graph[node]):
        if neighbor not in seen:
            seen.add(neighbor)
            path.append(neighbor)
            dfs(neighbor)
    if len(seen) == n:
        return 

dfs(v)
for i in range(len(path)):
    print(path[i], end=' ')


# BFS
seen = set([v])
path = [v]

def bfs(graph):
    import collections
    queue = collections.deque([v])
    while queue:
        node = queue.popleft()
        for neighbor in sorted(graph[node]):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
                path.append(neighbor)

bfs(graph)
print()
for i in range(len(path)):
    print(path[i], end=' ')

