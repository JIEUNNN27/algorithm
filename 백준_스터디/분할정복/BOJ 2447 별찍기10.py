# https://www.acmicpc.net/problem/2447
# https://day0522.github.io/posts/BOJ-2447/

import sys
input = sys.stdin.readline

N = int(input())

def solution(n):
    if n == 1:
        return '*'

    stars = solution(n//3) # 이전 단계의 별의 패턴을 저장(재귀)
    result = []

    for s in stars:
        result.append(s * 3)

    for s in stars:
        result.append(s + ' ' * (n//3) + s)

    for s in stars:
        result.append(s * 3)

    return result

answer = solution(N)

print(*answer, sep="\n")