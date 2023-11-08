# https://www.acmicpc.net/problem/1260

N, M, V = map(int, input().split())

# 그래프 만들기
keys = [i+1 for i in range(N)]
values = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    values[a-1].append(b)    
    values[b-1].append(a)

#그래프 만들기 전에 요 소트 해주기
for i in values:
    i.sort()

graph = dict(zip(keys, values))

#print(graph)

#DFS, 재귀로 구현

def dfs(v, dfs_visited = []):
    dfs_visited.append(v)
    for j in graph[v]:
        if j not in dfs_visited:
            dfs(j, dfs_visited)
    return dfs_visited

#BFS, 스택으로 구현
def bfs(v, bfs_visited = []):
    bfs_visited.append(v)
    queue = []
    queue.append(v)
    #queue.append[v]
    while queue:
        v = queue.pop(0)
        for k in graph[v]:
            if k not in bfs_visited:
                bfs_visited.append(k)
                queue.append(k)
           # queue.append(k)
    return bfs_visited

print(*dfs(V))
print(*bfs(V))

