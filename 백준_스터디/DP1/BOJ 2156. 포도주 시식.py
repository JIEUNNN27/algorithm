# https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline
N = int(input())

podo = [0, 0, 0]
for _ in range(N):
    p = int(input())
    podo.append(p)

# 끝에가 i인 경우의 최대값
dp = [0]*(N+3)

# a b c d e f g h 

# d의 입장에서
# b + c => dp[d] = dp[c] (d 건너뜀)
# b + d => dp[d] = dp[b] + podo[d] (c 건너뜀)
# c + d => dp[d] = dp[a] + podo[c] + podo[d] (b 건너뜀)


for i in range(3,N+3):
    # max(d 건너뜀, c 건너뜀, b 건너뜀)
    # max(dp[i-1], dp[i-2]+podo[i], dp[i-3]+podo[i-1]+podo[i])
    dp[i] = max(dp[i-1], dp[i-2]+podo[i], dp[i-3]+podo[i-1]+podo[i])
    #print(dp)


print(max(dp))