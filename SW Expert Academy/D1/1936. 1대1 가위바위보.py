#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
A, B = map(int, input().split())
#가위는 1, 바위는 2, 보는 3
if A-B==1 or A-B==-2:
    print("A")
else:
    print("B")