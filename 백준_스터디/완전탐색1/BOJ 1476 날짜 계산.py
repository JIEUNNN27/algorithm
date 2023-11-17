# https://www.acmicpc.net/problem/1476

E, S, M = map(int, input().split())

#1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

# y = 15

# if E == S and S == M:
#     print(E)

# else:
#     # while True:
#     #     y += 1
#     #     if y%15 == E and y%28 == S and y%19 == M:
#     #         print(y)
#     #         break
#     for i in range(1, 15*28*19+1):
#         if E == 15 and S != 28 and M != 19:
#             if i%15 == 0 and i%28 == S and y%19 == M:
#                 print(i)
#                 break
#         elif E != 15 and S == 28 and M != 19:
#             if i%15 == E and i%28 == 0 and y%19 == M:
#                 print(i)
#                 break
#         elif E != 15 and S != 28 and M == 19:
#             if i%15 == E and i%28 == S and y%19 == 0:
#                 print(i)
#                 break
#         elif E == 15 and S == 28 and M != 19:
#             if i%15 == 0 and i%28 == 0 and y%19 == M:
#                 print(i)
#                 break
#         elif E == 15 and S != 28 and M == 19:
#             if i%15 == 0 and i%28 == S and y%19 == 0:
#                 print(i)
#                 break
#         elif E != 15 and S == 28 and M == 19:
#             if i%15 == E and i%28 == 0 and y%19 == 0:
#                 print(i)
#                 break
#         elif E == 15 and S == 28 and M == 19:
#             print(7980)
#             break
#         else:
#             if i%15 == E and i%28 == S and i%19 == M:
#                 print(i)
#                 break


# https://data-flower.tistory.com/54
y = 0
while True:
    y += 1
    if (y-E)%15==0 and (y-S)%28==0 and (y-M)%19==0:
        print(y)
        break