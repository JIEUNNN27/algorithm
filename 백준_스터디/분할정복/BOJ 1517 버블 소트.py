# https://www.acmicpc.net/problem/1517
import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

#print(lst)

lst_sorted = sorted(lst)

#print(lst_sorted)

cnt = 0
while lst != lst_sorted:
    for i in range(N-1):
        x = lst[i]
        y = lst[i+1]
        if x>y:
            lst[i] = y
            lst[i+1] = x
            cnt += 1

        #print(lst)
print(cnt)

####--------위에 코드 -> 틀림

# https://blog.naver.com/mion0602/223221463503
# https://ojt90902.tistory.com/528


import sys
input = sys.stdin.readline
def devide(l,r) : 
    if l == r :
        return
    mid = (l + r)//2
    devide(l,mid)
    devide(mid+1,r)
    swap(l,mid,mid+1,r)
    return

def swap(ll,lr,rl,rr) :
    global swap_cnt
    temp_list = []
    start_idx = ll #이 변수는 현재 temp_list의 위치를 알려주는 값으로 보면 된다. 0이나 temp_list의 길이로 하지 않는 이유는 ll이 0부터 시작하지 않기 때문이다. 
    si,li = ll,rr #si : start_index의 줄임말. li : last_index의 줄임말. 둘다 원래 배열에 값을 넣을 때 사용한다. 
    while ll <= lr and rl <= rr : #좌,우 배열 중 한쪽 배열이 temp_list에 다 들어갈 때까지 값을 비교한다.
        if my_list[ll] > my_list[rl] : #오른쪽 배열에 있는 값을 temp_list에 집어넣는다.
            temp_list.append(my_list[rl])
            swap_cnt += (rl-start_idx)
            rl +=1 #
            start_idx +=1 
        else :
            temp_list.append(my_list[ll])
            ll += 1
            start_idx += 1
    while ll <= lr : #만약 왼쪽 배열이 temp_list로 덜 들어갔다면, 다 넣어준다.
        temp_list.append(my_list[ll])
        ll +=1
    while rl <= rr : #만약 오른쪽 배열이 temp_list로 덜 들어갔다면, 다 넣어준다.
        temp_list.append(my_list[rl])
        rl += 1
    for z in range(li,si-1,-1) : #temp_list에 넣어준 값을 하나씩 원래 배열로 넣어서 정렬시켜준다.
        my_list[z] = temp_list.pop()
    return


t = int(sys.stdin.readline().rstrip())
my_list = list(map(int,input().split()))
swap_cnt = 0
devide(0,len(my_list)-1)
print(swap_cnt)