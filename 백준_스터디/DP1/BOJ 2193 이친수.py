# https://www.acmicpc.net/problem/2193
N = int(input())

an_1 = 1
an_2 = 1

n_count = 2
an = 0


while True:
    if N == 1 or N == 2:
        print(1)
        break
    
    if n_count == N:
        print(an)
        break
    an = an_1+an_2
    an_2 = an_1
    an_1 = an
    n_count += 1