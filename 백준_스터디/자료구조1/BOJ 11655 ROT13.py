#https://www.acmicpc.net/problem/11655

#영어 알파벳을 13글자씩 밀어서 만든다.

#https://velog.io/@slbin-park/%EB%B0%B1%EC%A4%80-11655%EB%B2%88-ROT13-%ED%8C%8C%EC%9D%B4%EC%8D%AC

n = input()
res = ''
for i in range(len(n)):
    if n[i] == ' ' or ord(n[i]) < ord('A'):
        res += n[i]
    else:
        if ord(n[i]) + 13 > 122:
            res += chr(96 + (ord(n[i]) + 13) - 122)
        elif ord(n[i]) + 13 > 90 and ord(n[i]) < 91:
            res += chr(64 + (ord(n[i]) + 13) - 90)
        else:
            res += chr(ord(n[i]) + 13)
print(res)