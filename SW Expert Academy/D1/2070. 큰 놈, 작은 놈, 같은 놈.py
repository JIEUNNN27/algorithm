# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a < b:
        print(f"#{i+1} <")
    elif a == b:
        print(f"#{i+1} =")
    else:
        print(f"#{i+1} >")