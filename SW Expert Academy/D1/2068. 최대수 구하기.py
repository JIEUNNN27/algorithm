#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    print(f"#{i+1} {max(data)}")
