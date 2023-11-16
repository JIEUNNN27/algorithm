# https://www.acmicpc.net/problem/7785

# n = int(input())

# company = []

# for i in range(n):
#     name, door = input().split()
#     if door == "enter":
#         company.append(name)
#     elif door == "leave":
#         company.remove(name)

# company.sort(reverse=True)
# print(*company, sep = "\n")

#########시간 초과###############
# import sys
# input = sys.stdin.readline
# n = int(input())

# company = []

# for i in range(n):
#     name, door = input().split()
#     if door == "enter":
#         company.append(name)
#     elif door == "leave":
#         company.remove(name)

# company.sort(reverse=True)
# print(*company, sep = "\n")

#########시간 초과###############
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())

# company = deque()

# for i in range(n):
#     name, door = input().split()
#     if door == "enter":
#         company.append(name)
#     elif door == "leave":
#         company.remove(name)

# answer = deque(sorted(company, reverse=True))
# print(*answer, sep = "\n")

#########시간 초과###############
import sys

input = sys.stdin.readline

n = int(input())

company = {}

for i in range(n):
    name, door = input().split()
    if door == "enter":
        company[name] = 1
    elif door == "leave":
        del company[name]

answer = list(company.keys())
answer.sort(reverse=True)
print(*answer, sep = '\n')