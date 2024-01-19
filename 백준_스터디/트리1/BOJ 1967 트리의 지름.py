# https://www.acmicpc.net/problem/1967
# https://kyun2da.github.io/2021/05/04/tree's_diameter/

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

# 트리 만들기
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])


def dfs(x, w):
    for i in tree[x]:
        a, b = i
        # if distance[a] == 0: => 틀림
        if distance[a] == -1:  
            distance[a] = w + b
            dfs(a, w + b)
            #print(distance)


# 1번 노드에서 가장 먼 곳을 찾는다.

# distance 초기값 0으로 하면 틀림 -> -1로 해야함
# distance = [0] * (n + 1) => 틀림
distance = [-1]*(n+1)
distance[1] = 0
dfs(1, 0)


# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
# distance = [0] * (n + 1) => 틀림
distance = [-1]*(n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))