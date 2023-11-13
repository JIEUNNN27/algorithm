# https://www.acmicpc.net/problem/2178
# 참고코드 https://security-guide.tistory.com/124

from collections import deque

# N, M input 받기
N, M = map(int, input().split())

# miro 리스트로 그리기
miro = []
for _ in range(N):
    #miro.append([int(x) for x in input()])
    temp = []
    s = input()
    for i in s:
				#여기에서 int 안하면 답이 틀림..!
        temp.append(int(i))
    miro.append(temp)

    # 위에 코드를 이걸로 축약 가능
    # miro.append(list(map(int, input().split())))
#print(miro)

# 상하좌우 이동을 리스트로 표현하기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문 리스트
visited = [[0 for _ in range(M)] for _ in range(N)]


def bfs(x, y, count):
    queue = deque()
    queue.append([y, x, count])
    

    while queue:
        # print(queue)
        # print(visited)
        # print(count)
        # 가장 앞에 들어 있는 애들
        y, x, count = queue.popleft()

        # 목표 위치에 도달하면
        if y == N - 1 and x == M - 1:
            return count+1
        
        # 상하좌우 위치 이동
        for i in range(4):
            
            # 상하좌우 이동한 위치
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치 벗어났을 때
            if nx < 0 or ny < 0 or ny>=N or nx>=M:
                continue
            
            # 벽일때
            if miro[ny][nx] == 0:
                continue

            # 이미 방문한 곳일 때
            if visited[ny][nx] == 1:
                continue


            queue.append([ny, nx, count+1])
            visited[ny][nx] = 1
        
    return -1

print(bfs(0,0,0))