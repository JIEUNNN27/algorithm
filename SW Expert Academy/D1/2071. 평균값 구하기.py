# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2

t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    print(f"#{i+1} {round(sum(data)/10)}")

#int랑 round 차이