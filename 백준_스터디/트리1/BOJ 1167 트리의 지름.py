# https://www.acmicpc.net/problem/1167
# https://blog.naver.com/zlsoq/223300898831

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

V = int(input())

tree = [[]*V for _ in range(V+1)]
visited = [-1]*(V+1)

def dfs(v, w):
    for n, l in tree[v]:
        cost = w + l
        if visited[n] == -1:
            visited[n] = cost
            dfs(n, cost)

for i in range(1, V+1):
    temp = list(map(int, input().rstrip().split()))
    for j in range(1, len(temp), 2):
        if temp[j] == -1:
            continue
        else:
            tree[temp[0]].append((temp[j], temp[j+1]))

visited[1] = 0

dfs(1, 0)

idx = visited.index(max(visited))

visited = [-1]*(V+1)
visited[idx] = 0

dfs(idx, 0)

print(max(visited))