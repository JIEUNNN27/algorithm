# https://www.acmicpc.net/problem/11724
# https://blog.naver.com/cody628/223231864281

import sys
# 런타임 에러 해결
sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
N, M = map(int, input().split())


# 그래프 만들기
# 방향 없는 그래프 -> 양뱡향으로 그래프에 넣어주기
keys = [i+1 for i in range(N)]
values = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    values[a-1].append(b)
    values[b-1].append(a)

graph = dict(zip(keys, values))

#print(graph)

# 방문 체크
visited = [0]*(N+1)

#dfs
def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] != 1:
            dfs(i)
    return visited

cnt = 0
for j in range(1, N+1):
    if visited[j] != 1:
        cnt += 1
        dfs(j)
        # print(dfs(j))

print(cnt)

