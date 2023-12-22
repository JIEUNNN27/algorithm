# https://www.acmicpc.net/problem/2225

# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수

# DP 어려워서,,순열과 조합으로 풀었는데 맞았어요,,


# 중복을 허용하고 n개중 r개를 순서있게 나열
# from itertools import product

# N, K = map(int, input().split())

# temp = [i for i in range(N+1)]

# lst = list(product(temp, repeat=K))
# answer = 0
# for i in lst:
#     if sum(i) == N:
#         #print(i)
#         answer += 1
# #print(len(lst))
# print(answer)

# ===> 메모리 초과

# N, K = map(int, input().split())
# # a = (N+1)+(K-1)-1
# a = N+K-1
# b = K-1

# bunmo = 1
# bunza = 1
# if K == 1:
#     print(1)

# else:

#     for i in range(1, K):
        
#         # print(a)
#         # print(b)
#         bunmo *= a
#         bunza *= b

#         a = a-1
#         b = b-1

#     print(int(bunmo/bunza)%1000000000)




# https://www.acmicpc.net/problem/2225

# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수

N,K = map(int,input().split(" "))

def hab(N,a):
    ans = 1; div = 1
    if a == 0:
        return 1
    for i in range(1,a+1):
        ans *= N
        div *= i
        N -= 1
    return int(ans//div)

answer = 0
for i in range(1,K+1):
    answer += (hab(N-1,i-1) * hab(K,K-i))
print(answer% 1000000000)