# https://www.acmicpc.net/problem/9465
# https://blog.naver.com/ej_0109/222698134863

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(2)]
    
    # dp -> i행, j열까지의 최대값/ 초기값 자기 자신. dp 대신 lst 고대로 해도 됨
    dp = lst

    if N!=1:
        dp[0][1] = dp[0][1] + dp[1][0]
        dp[1][1] = dp[0][0]+dp[1][1]
    
        for i in range(2, N):
            # max(바로직전 대각선 거치는 경우, 바로직전전 대각선 거치는 경우)
            dp[0][i] = max(dp[0][i]+dp[1][i-1], dp[0][i]+dp[1][i-2])
            dp[1][i] = max(dp[1][i]+dp[0][i-1], dp[1][i]+dp[0][i-2])
            #print(dp)
    
    # 인덱스는 0부터 시작하는거 고려
    print(max(dp[0][N-1], dp[1][N-1]))