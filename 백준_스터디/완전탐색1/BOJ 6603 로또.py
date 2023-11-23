#https://www.acmicpc.net/problem/6603
from itertools import combinations
while True:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break

    k = lst.pop(0)

    #print(k)
    #print(lst)

    lotto = list(combinations(lst, 6))
    #print(lotto)
    
    for i in lotto:
        answer = list(i)
        print(*answer)
    print()