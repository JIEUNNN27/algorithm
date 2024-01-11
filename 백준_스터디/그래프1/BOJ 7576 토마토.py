# https://www.acmicpc.net/problem/7576
# https://blog.naver.com/bellepoque7/223011531895


import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
m,n = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)] 

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))
            visited[i][j] = 1


dy = [-1,1,0,0]
dx = [0,0,-1,1]
cnt = 0

def bfs():
    global cnt
    while queue:
        for i  in range(len(queue)):
            r,c = queue.popleft()
            for i in range(4):
                ny = r + dy[i]
                nx = c + dx[i]
                if ny < n and nx < m and ny >=0 and nx >=0 and graph[ny][nx] == 0 and visited[ny][nx] == 0:
                    # print(ny,nx)
                    visited[ny][nx] = visited[r][c] + 1
                    queue.append((ny,nx))
                    
                # print(visited)
        cnt += 1
        

# 덜익은 토마토가 있는지 없는지 체크
def check():
    for i in range(n):
        for j in range(m):
            # 방문하지도 않(못)했고, 덜익은 토마토가 있다면
            if visited[i][j] == 0 and graph[i][j]==0:
                print(-1)
                return
    print(cnt-1)

bfs()
check()