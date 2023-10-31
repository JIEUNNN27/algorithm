# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
t = int(input())
for i in range(t):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N !=1 :
        if N%2 == 0:
            a += 1
            N = N/2
        elif N%3 == 0:
            b += 1
            N = N/3
        elif N%5 == 0:
            c += 1
            N = N/5
        elif N%7 == 0:
            d += 1
            N = N/7
        elif N%11 == 0:
            e += 1
            N = N/11
    print(f"#{i+1} {a} {b} {c} {d} {e}")