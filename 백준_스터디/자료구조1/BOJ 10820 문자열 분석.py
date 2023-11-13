# https://www.acmicpc.net/problem/10820

while True:
    try:
        st = input()
        small = 0
        big = 0
        num = 0
        blank = 0
        for i in st:
            if i.islower():
                small += 1
            elif i.isupper():
                big += 1
            elif i.isdigit():
                num += 1
            elif i.isspace():
                blank += 1

        print(small, big, num, blank)

    except:
        break