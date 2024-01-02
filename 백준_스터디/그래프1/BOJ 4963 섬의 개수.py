# https://www.acmicpc.net/problem/4963
# https://star7sss.tistory.com/406

import sys
from collections import deque
input = sys.stdin.readline

w = 1
h = 1
# 상하좌우, 대각선 방향
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, -1, 1, 1]




while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    cnt = 0
    
    for i in range(h):
       for j in range(w):
            # visited[i][j] = 1

            # 땅이 있으면
            if graph[i][j] == 1:
                cnt += 1
                queue = deque([(i, j)])
                graph[i][j] = 0

                # 상하좌우, 대각선 이동
                while queue:
                    y, x = queue.popleft()


                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        #범위 안에서
                        if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == 1:
                            graph[ny][nx] = 0
                            queue.append((ny, nx))

                            
    print(cnt)