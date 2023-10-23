# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PhcWaAKIDFAUq&categoryId=AV5PhcWaAKIDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
N = int(input())

for i in range(1, N+1):
    if N%i == 0:

        #print에 end 옵션 기억하기
        print(i, end = " ")
