# https://www.acmicpc.net/problem/9095
# 1 1 (1)
# 2 1+1, 2 (2)
# 3 1+1+1, 1+2, 2+1 (4)
# 4 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1 (7)
# 5 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1, 2+3, 3+2, 3+1+1, 1+3+1, 1+1+3 (13)

T = int(input())

lst = [1, 2, 4]
#  n은 양수이며 11보다 작다.

for i in range(3, 12):
    a, b, c = i-1, i-2, i-3
    x = lst[a]+lst[b]+lst[c]
    lst.append(x)
    #print(x)
    

#print(lst)

for i in range(T):
    n = int(input())
    print(lst[n-1])
