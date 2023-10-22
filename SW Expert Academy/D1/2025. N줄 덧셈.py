#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AV5QFZtaAscDFAUq&categoryId=AV5QFZtaAscDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
#주어진 숫자까지 1부터 다 더하기
a = int(input())
s = 0
for i in range(1, a+1):
    s += i
    
print(s)