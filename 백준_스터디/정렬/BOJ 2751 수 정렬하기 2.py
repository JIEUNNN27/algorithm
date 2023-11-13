# https://www.acmicpc.net/problem/2751

#입력을 sys로 바꿔주기
import sys
N = int(sys.stdin.readline())

lst = []
for i in range(N):
    x = int(sys.stdin.readline())
    lst.append(x)

lst.sort()

print(*lst, sep='\n')