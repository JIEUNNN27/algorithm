# https://www.acmicpc.net/problem/11004
N, K = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
print(lst[K-1])
