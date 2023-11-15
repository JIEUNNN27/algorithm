#https://www.acmicpc.net/problem/11651

N = int(input())

dict = {}
for i in range(N):
    dict[i] = list(map(int, input().split()))
so = sorted(dict.items(), key = lambda x:(x[1][1], x[1][0]))

for i in so:
    print(*i[1])