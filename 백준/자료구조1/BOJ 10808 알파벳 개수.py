#https://www.acmicpc.net/problem/10808
S = input()
lst = []
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [0 for _ in range(26)]
for i in S:
    lst.append(i)

dict = {}

for i in S:
    for j in alpha:
        if i == j:
            # index 함수
            idx = alpha.index(j)
    answer[idx] += 1

print(*answer)

