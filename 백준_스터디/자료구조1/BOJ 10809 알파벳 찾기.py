# https://www.acmicpc.net/problem/10809
S = input()
lst = []
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [-1 for _ in range(26)]

for i in S:
    lst.append(i)

for j in alpha:
    a = alpha.index(j)
    if j in lst:
        x = lst.index(j)
        #print(x)
        answer[a] = x

print(*answer)
