# https://www.acmicpc.net/problem/11055
# # 1. 증가하는 수열만 모으기
# # 2. 합이 큰 것만 출력하기

# N = int(input())

# lst = list(map(int, input().split()))

# # i번째에서 시작
# sum_lst = []
# for i in range(N):
#     temp = [i]
#     for j in range(i, N):
#         if lst[j] > temp[-1]:
#             temp.append(lst[j])
#     sum_lst.append(sum(temp))

# print(max(sum_lst))

# https://bmy1320.tistory.com/entry/%EB%B0%B1%EC%A4%80-Silver-2-%EB%AC%B8%EC%A0%9C-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-11055-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A6%9D%EA%B0%80-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4
import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
dp=[0 for i in range(N)]
dp[0]=A[0]

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i]=max(dp[i],A[i]+dp[j])
        else:
            dp[i]=max(dp[i],A[i])
print(max(dp))