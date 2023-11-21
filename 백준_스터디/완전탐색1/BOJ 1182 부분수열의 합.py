# https://www.acmicpc.net/problem/1182
import itertools
import sys
input = sys.stdin.readline
N, S = map(int, input().split())

nums = list(map(int, input().split()))
count = 0
for i in range(1, N+1):
    temp = list(itertools.combinations(nums, i))
    #print(temp)
    for j in temp:
        if sum(j) == S:
            count += 1

print(count)