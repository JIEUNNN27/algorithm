# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    s = 0
    for j in range(len(data)):
        if data[j]%2==1:
            s+=data[j]
    print(f"#{i+1} {s}")