# https://www.acmicpc.net/problem/10844
# https://blog.naver.com/cody628/223282482777

# 0 1 2 3 4 5 6 7 8 9 로 끝나는 숫자 개수
# N = 1
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# N = 2
# [1, 1, 2, 2, 2, 2, 2, 2, 2, 1]
# N = 3
# [1, 3, 3, 4, 4, 4, 4, 4, 3, 2]
# N = 4
# [3, 4, 7, 7, 8, 8, 8, 7, 6, 3]

import sys
input = sys.stdin.readline

N = int(input())

# N -> 에러 N+1 -> 에러
dp = [[0 for i in range(10)] for j in range(N+2)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp[2] = [1, 1, 2, 2, 2, 2, 2, 2, 2, 1]

if N >2:
    for i in range(3, N+1):
        for j in range(0, 10):
            if j == 0:
                dp[i][1] += dp[i-1][0]
            elif j == 9:
                dp[i][8] += dp[i-1][9]
            else:
                dp[i][j+1] += dp[i-1][j]
                dp[i][j-1] += dp[i-1][j] 
#print(*dp, sep = "\n")
print(sum(dp[N])%1000000000)