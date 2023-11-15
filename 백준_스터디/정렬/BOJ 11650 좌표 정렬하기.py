#https://www.acmicpc.net/problem/11650
#이것도 이거 사용 sorted(dict.items(), key = lambda x:(x[1][0], x[1][1]))

N = int(input())

dict = {}

for i in range(N):
    dict[i] = list(map(int, input().split()))

#print(dict)

dict2 = sorted(dict.items(), key = lambda x:(x[1][0], x[1][1]))

#print(dict2)

for i in range(N):
   print(*dict2[i][1])