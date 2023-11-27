# https://www.acmicpc.net/problem/2331
A, P = map(int, input().split())

lst = [A]

#print(lst[-1])
while True:    
    temp_i = str(lst[-1])
    temp_x = 0
    for j in temp_i:
        j = int(j)
        temp_x += j**P
    lst.append(temp_x)

    if len(lst)!=len(set(lst)):
        break

#print(lst)

lst_check = []
for k in lst:
    if k not in lst_check:
        lst_check.append(k)
    else:
        from_here = k
        break

idx = lst_check.index(k)

print(len(lst[:idx]))