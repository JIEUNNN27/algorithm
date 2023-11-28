# https://www.acmicpc.net/problem/11727
N = int(input())

lst = [1, 1]
def answer(x, lst):
    if x == 1:
        return 1
    else:
        for i in range(1, N):
            lst.append(lst[-2]*2+lst[-1])
        return lst[-1]
    
#10,007로 나눈 나머지 출력하는거 잊지 말것..
print(answer(N, lst)%10007)