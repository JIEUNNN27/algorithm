# https://www.acmicpc.net/problem/10814
# N = int(input())

# dict = {}
# for i in range(N):
#     age, name = input().split()
#     age = int(age)
#     dict[name] = age

# dict2 = sorted(dict.items(), key= lambda x: x[1])

# for i in range(N):
#     print(dict2[i][1], dict2[i][0])

##########런타임 에러####################
# N = int(input())

# lst = []
# for i in range(N):
#     age, name = input().split()
#     age = int(age)
#     lst.append([age, name])

# lst2 = sorted(lst, key= lambda x: x[0])

# for i in range(N):
#     print(f"{lst2[i][0]} {lst2[i][1]}", sep = '\n')

#############속도 증가######################
import sys
input = sys.stdin.readline
N = int(input())

lst = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    lst.append([age, name])

lst2 = sorted(lst, key= lambda x: x[0])

for i in range(N):
    print(f"{lst2[i][0]} {lst2[i][1]}", sep = '\n')