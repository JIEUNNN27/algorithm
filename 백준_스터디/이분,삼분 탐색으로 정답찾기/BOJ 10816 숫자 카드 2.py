# https://www.acmicpc.net/problem/10816
# https://blog.naver.com/rhkr_alswjd/222665524982


# 시간 초과
# import sys

# n = int(input())
# n_list = [int(_) for _ in sys.stdin.readline().split()]
# n_list.sort()

# m = int(input())
# m_list = [int(_) for _ in sys.stdin.readline().split()]

# for i in m_list:
#     print(n_list.count(i), end = ' ')


# https://infinitt.tistory.com/288

import sys

input = sys.stdin.readline

N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

answer = dict()

for i in n_lst:
    try :
        answer[i] += 1
    except:
        answer[i] = 1

for i in m_lst:
    try:
        print(answer[i] , end = " ")
    except:
        print(0, end=" ")
    

