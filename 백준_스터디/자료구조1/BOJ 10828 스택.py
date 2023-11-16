# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    order = list(input().split())

    if order[0] == "push":
        stack.append(order[1])
    
    if order[0] == "pop":
        if stack != []:
            x = stack.pop()
            print(x)
        else:
            print(-1)
    
    if order[0] == "size":
        print(len(stack))
    
    if order[0] == "empty":
        if stack != []:
            print(0)
        else:
            print(1)
    
    if order[0] == "top":
        if stack != []:
            print(stack[-1])
        else:
            print(-1)