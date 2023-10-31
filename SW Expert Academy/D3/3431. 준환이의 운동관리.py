# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
t = int(input())
for i in range(t):
    L, U, X = map(int, input().split())
    if X > U :
        print(f"#{i+1} -1")
    elif X < L :
        print(f"#{i+1} {L-X}")
    else:
        print(f"#{i+1} 0")