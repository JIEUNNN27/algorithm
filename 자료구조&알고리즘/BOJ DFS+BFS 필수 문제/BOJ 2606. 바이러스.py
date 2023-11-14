#https://www.acmicpc.net/problem/2606

#dfs

N = int(input())
C = int(input())

keys = [i+1 for i in range(N)]
values = [[] for _ in range(N)]

for i in range(C):
    a, b = map(int, input().split())
    values[a-1].append(b)
    values[b-1].append(a)

graph = dict(zip(keys, values))

#print(graph)

def dfs(start, visited=[]):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            visited = dfs(i, visited)
    return visited

print(len(dfs(1))-1)