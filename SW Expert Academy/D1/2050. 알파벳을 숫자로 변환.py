# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLGxKAzQDFAUq&categoryId=AV5QLGxKAzQDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
s = input()
for i in range(len(s)):
    print(ord(s[i])-64, end = " ")