#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
t = int(input())
for i in range(t):
    s = input()
    if s == s[::-1]:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")

