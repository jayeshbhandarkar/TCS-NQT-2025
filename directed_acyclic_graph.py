from collections import defaultdict, deque

def shortest_path_dag(n, edges, src, dest):
    graph = defaultdict(list)
    indegree = [0] * n
    
    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    dist = [float('inf')] * n
    dist[src] = 0
    parent = [-1] * n

    for u in topo_order:
        if dist[u] != float('inf'):
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    parent[v] = u

    path = []
    temp = dest
    while temp != -1:
        path.append(temp)
        temp = parent[temp]
    path.reverse()

    print("Path:", " -> ".join(map(str, path)))
    print("Total weight:", dist[dest])

n, e = map(int, input().split())
edges = []

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

src = int(input())
dest = int(input())
shortest_path_dag(n, edges, src, dest)
