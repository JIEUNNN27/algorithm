# https://www.acmicpc.net/problem/11729
# https://study-all-night.tistory.com/6

    
N = int(input())

def hanoi(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi(n-1, 6-start-end, end) # 3단계

print(2**N-1)
hanoi(N, 1, 3)