# https://www.acmicpc.net/problem/10971
# https://m.blog.naver.com/anytime0916/222910034692


import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n
answer = float('inf')

def DFS(v, cost):
    global answer
    visit[v] = 1
    # graph[v][i] != 0 조건 없으면 틀림
    if sum(visit) == n and graph[v][i] != 0:
    #print(visit)
    #if sum(visit) == n: 
        answer = min(answer, cost+graph[v][i])
    else:
        for j in range(n):
            if visit[j] == 0 and graph[v][j] != 0:
                DFS(j, cost+graph[v][j])
    visit[v] = 0


for i in range(n):
    DFS(i, 0)

print(answer)