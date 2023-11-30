# https://www.acmicpc.net/problem/9461

T = int(input())

lst = [1, 1, 1]

# 수열 리스트로 먼저 만들기
for k in range(100):
    x = lst[-3] + lst[-2]
    lst.append(x)

#print(lst)

for i in range(T):
    N = int(input())
    print(lst[N-1])