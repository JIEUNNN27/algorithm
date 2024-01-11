# https://www.acmicpc.net/problem/2146
# https://blog.naver.com/bellepoque7/223010953323

#목표 dfs로 각 섬을 숫자로 바꾸기 
import sys
#기본 재귀가 너무많이 들어가므로 리밋올리기
sys.setrecursionlimit(10**9)
from itertools import *

#그래프 좌표 넣을 2d array
graph = []
#섬(1)의 좌표 넣을 리스트, 추후 큐 형태로 순환할 것
island = []
#나중에 섬의 위치 좌표 넣을 리스트 생성
corrd_comb = []
min_dist = 10e9
n = int(input())
visited = [[0]*n]*n

#섬 좌표 받기
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# print(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            island.append((i,j))
# print(island) #섬의 좌표 
# [(0, 0), (0, 1), (0, 2), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 8), (1, 9), (2, 0), (2, 2), (2, 3), (2, 8), (2, 9), (3, 2), (3, 3), (3, 4), (3, 9), (4, 3), (4, 9), (5, 9), (7, 4), (7, 5), (8, 4), (8, 5), (8, 6)] 

# 일단 모두 좌표를 돌면서 dfs로 재귀할거고... 
# 만약에 좌표가 0이면 멈추고 탈출할거고 그다음에 다른 좌표로 갈거임

dr = [-1,1,0,0] #상하좌우 
dc = [0,0,-1,1]

is_num = 2
def dfs(r,c,is_num):
    graph[r][c] = is_num
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < n and nc < n and nr >=0 and nc >=0:
            if graph[nr][nc] == 1 and visited[nr][nc] == 0:
                #섬 좌표있으면 어짜피 탐색할거니까 지워 
                if (nr,nc) in island:
                    island.remove((nr,nc))
                dfs(nr,nc,is_num)
                # print('end')
    #재귀 끝날때마다 그래프 확인하려면 하기 주석 제거 
    # for i in range(n):
    #     print(graph[i])
    # print('----')
    return 

#그래프를 변형하되 섬마다 2,3,4 라고 표기하기
for i in island:
    dfs(i[0],i[1],is_num)
    is_num += 1

#각 섬의 좌표를 조합으로 만들어서 xy좌표의 기준 벡터 최소값 구하기
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            corrd_comb.append((i,j,graph[i][j]))

for i in combinations(corrd_comb,2):
    if i[0][2] != i[1][2]:
        min_dist = min(min_dist, abs(i[0][0]-i[1][0]) + abs(i[0][1]-i[1][1])-1)
print(min_dist)
