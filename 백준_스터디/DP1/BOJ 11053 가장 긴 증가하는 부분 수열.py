# https://www.acmicpc.net/problem/11053
import sys
input = sys.stdin.readline
N = int(input())

lst = list(map(int, input().split()))

# 자기 자신을 끝으로 할 때 가장 긴 증가하는 부분수열의 길이
# 를 저장하면서 진행
dp = [1]*N


for i in range(N):
    # lst[i]가 수열의 끝
    #print(i)
    for j in range(i):
        if lst[i]>lst[j]:
            dp[i] = max(dp[i], dp[j]+1)
        #print(dp)

print(max(dp))