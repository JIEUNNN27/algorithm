#https://www.acmicpc.net/problem/10819
import itertools
N = int(input())
arr = list(map(int, input().split()))

itt = list(itertools.permutations(arr, N))

#print(itt)

answer = 0

for i in itt:
    temp_sum = 0
    for j in range(N-1):
        temp_sum += abs(i[j]-i[j+1])

    if temp_sum > answer:
        answer = temp_sum

print(answer)