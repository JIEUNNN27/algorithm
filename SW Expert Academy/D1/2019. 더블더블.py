# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QDEX6AqwDFAUq&categoryId=AV5QDEX6AqwDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2

n = int(input())
p = 1
print(p, end = " ")
for i in range(1, n+1):
    p *= 2
    print(p, end = " ")