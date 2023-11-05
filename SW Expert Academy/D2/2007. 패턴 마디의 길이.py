#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

t = int(input())

for i in range(t):
    s = input()
    for j in range(1,11):
        if s[:j]==s[j:2*j]:
            print(f"#{i+1} {j}")
            break
