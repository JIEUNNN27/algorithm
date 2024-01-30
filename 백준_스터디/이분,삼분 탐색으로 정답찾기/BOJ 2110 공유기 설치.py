# https://www.acmicpc.net/problem/2110
# https://post.naver.com/viewer/postView.naver?volumeNo=27501500&memberNo=33264526&vType=VERTICAL

import sys
input = sys.stdin.readline
N, C = map(int, input().split())

lst = []

for i in range(N):
    lst.append(int(input()))

lst.sort()

start, end = 1, lst[-1] - lst[0]

answer = 0

while start <= end:
    mid = (start+end) // 2

    idx, result = 0, 1

    for j in range(1, len(lst)):
        if lst[idx] + mid <= lst[j]:
            result += 1
            idx = j

    if result < C:
        end = mid -1
    else:
        answer = mid
        start = mid + 1

print(answer)