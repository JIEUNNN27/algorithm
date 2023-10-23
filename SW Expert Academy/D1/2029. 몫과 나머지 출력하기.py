#https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
#2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f"#{i+1} {a//b} {a%b}")
