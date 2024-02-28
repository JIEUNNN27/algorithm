# https://www.acmicpc.net/problem/1744

# 내 베프 gpt가 풀어준 코드

import sys
input = sys.stdin.readline
n = int(input())
positive = []
negative = []
ones = 0
result = 0

for _ in range(n):
    number = int(input())
    if number > 1:
        positive.append(number)
    elif number == 1:
        ones += 1
    else:
        negative.append(number)

positive.sort(reverse=True)
negative.sort()

# 양수 처리
for i in range(0, len(positive), 2):
    if i + 1 < len(positive):
        result += positive[i] * positive[i+1]
    else:
        result += positive[i]

# 음수 처리
for i in range(0, len(negative), 2):
    if i + 1 < len(negative):
        result += negative[i] * negative[i+1]
    else:
        result += negative[i]

# 1 더하기
result += ones

print(result)