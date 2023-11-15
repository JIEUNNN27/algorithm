# https://www.acmicpc.net/problem/11652
# 해시
# 이 문제도 sorted(dict.items(), key=lambda x:(-x[1], x[0])) 이용하기

N = int(input())
dict = {}
for i in range(N):
    x = int(input())
    if x not in dict.keys():
        dict[x] = 1
    else:
        dict[x] += 1

dict2 = sorted(dict.items(), key=lambda x:(-x[1], x[0]))

print(dict2[0][0])