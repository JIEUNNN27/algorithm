# https://www.acmicpc.net/problem/10825
# https://data-flower.tistory.com/89

N = int(input())

dict = {}
for i in range(N):
    student = list(input().split())
    #print(student)
    dict[f"{student[0]}"] = [student[1], student[2], student[3]]

#print(dict)

#dict.items(), key=lambder x 이용하기,
#x가 여러개일때는 ()안에 여러개 넣기 가능
#내림차순 정렬은 -x

sort_korean = sorted(dict.items(), key=lambda x: (-int(x[1][0]), int(x[1][1]), -int(x[1][2]), x[0]))

for i in sort_korean:
    print(i[0])