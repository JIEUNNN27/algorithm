# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
t = int(input())
for i in range(t):
    P, Q, R, S, W = map(int, input().split())

    A = P*W
    B = 0
    if W <= R:
        B = Q
    else:
        B = Q + (W-R)*S

    print(f"#{i+1} {min(A, B)}")

