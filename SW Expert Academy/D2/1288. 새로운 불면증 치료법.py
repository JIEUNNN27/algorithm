#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV18_yw6I9MCFAZN&categoryId=AV18_yw6I9MCFAZN&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
t = int(input())
for i in range(t):
    k = 0
    N = int(input())
    check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while check != []:
        k += 1
        sheep = k*N
        temp = str(sheep)

        for j in temp:
            n = int(j)
            if n in check:
                check.remove(n)


    print(f"#{i+1} {k*N}")