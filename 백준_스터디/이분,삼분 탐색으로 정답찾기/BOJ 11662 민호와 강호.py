# https://www.acmicpc.net/problem/11662
# https://velog.io/@bobsiunn/Search-11662%EB%B2%88-%EB%AF%BC%ED%98%B8%EC%99%80-%EA%B0%95%ED%98%B8-24%EC%9D%BC%EC%B0%A8


# #코드 실행 시간 단축을 위한 sys 모듈 import
# import sys
# #sqrt와 pow 사용을 위한 math 모듈 import
# import math
# input = sys.stdin.readline
# #민호의 출발점의 좌표(x1,y1)와 도착점의 좌표(x2,y2)
# #강호의 출발점의 좌표(x3,y3)와 도착점의 좌표(x4,y4)
# x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
# #출발점에서 p만큼 움직였을 때의 민호의 좌표를 반환하는 함수
# def minho(p):
#     #x좌표 = 출발점 x1에서 총 이동거리(x2-x1) 중 p%만큼의 거리를 더함
#     #y좌표 = 출발점 y1에서 총 이동거리(y2-y1) 중 p%만큼의 거리를 더함
#     return [x1 + (x2 - x1) * (p/100), y1 + (y2 - y1) * (p/100)]
# #출발점에서 p만큼 움직였을 때의 강호의 좌표를 반환하는 함수
# def kangho(p):
#     #x좌표 = 출발점 x3에서 총 이동거리(x4-x3) 중 p%만큼의 거리를 더함
#     #y좌표 = 출발점 y3에서 총 이동거리(y4-y3) 중 p%만큼의 거리를 더함
#     return [x3 + (x4 - x3) * (p/100), y3 + (y4 - y3) * (p/100)]

# #탐색 시작점의 이동 거리 비율(탐색이 이루어지지 않았기에 0%)
# fp = 0
# #탐색 종료점의 이동 거리 비율(탐색이 완료된 시점이기에 100%)
# lp = 100
# #민호와 강호 사이의 거리를 저장하는 변수(문제 기준 가능한 가장 큰 값으로 미리 설정)
# length =  math.sqrt(pow(10000, 2) + pow(10000, 2))
# #탐색 오차가 10의 -7승보다 작아질 때까지
# #탐색 종료점-탐색 시작점은 해당 구간 사이에 거리의 최솟값이 있어야 한다는 것을 의미(신뢰구간)
# #해당 구간으 길이가 10의 -7승보다 작아진다는 것은 오차 범위가 10^-6~10^-7 사이로 들어온다는 것을 의미한다
# while(lp-fp >= 1e-7):
#     #탐색 시작점과 종료점을 2:1로 내분하는 점 k1
#     k1 = (fp*2 + lp)/3
#     #탐색 시작점과 종료점을 1:2로 내분하는 점 k2
#     k2 = (fp + lp*2)/3
#     #시작점~k1 구간의 민호의 좌표 
#     m_k1 = minho(k1)
#     #시작점~k2 구간의 민호의 좌표
#     m_k2 = minho(k2)
#     #시작점~k1 구간의 강호의 좌표
#     k_k1 = kangho(k1)
#     #시작점~k2 구간의 강호의 좌표
#     k_k2 = kangho(k2)
#     #k1 구간에서의 민호와 강호의 거리
#     dist_k1 = math.sqrt(pow(m_k1[0] - k_k1[0],2) + pow(m_k1[1] - k_k1[1],2))
#     #k2 구간에서의 민호와 강호의 거리
#     dist_k2 = math.sqrt(pow(m_k2[0] - k_k2[0],2) + pow(m_k2[1] - k_k2[1],2))
#     #기존에 저장된 거리와 새로운 구간에서의 거리 중 작은 값중 작은 값을 새로운 길이로 저장
#     length = min(length, min(dist_k1, dist_k2))
#     #시작점~k1 구간에서의 거리가 시작점~k2 구간에서의 거리보다 멀면
#     if(dist_k1 >= dist_k2):
#         #시작점~k1구간에 최소값이 없으므로 다음 탐색 시작점을 k1으로 설정
#         fp = k1
#     #시작점~k1 구간에서의 거리가 시작점~k2 구간에서의 거리보다 가까우면
#     else:
#         #시작점~k2구간에 최소값이 없으므로 다음 탐색 종료점을 k2으로 설정
#         lp = k2
# #모든 탐색이 끝났을 때 민호와 강호 사이의 거리를 출력
# print('%.10f' %length)

# #인사이트
# #삼분 탐색 문제가 사용되기 위한 조건은 다음과 같다
# #탐색의 허용 오차 범위가 주어질 것
# #목표값을 볼록하거나 오목한 그래프로 나타낼 수 있어 최대값과 최소값이 존재할 때(미분값이 0인 지점)
# #시간 변수 t를 중심으로 연속적으로 값이 변화할때
# #해당 문제에는 사용되지 못했지만, 두 선분 사이의 교점 판정 알고리즘도 존재한다는 것을 깨달음


import sys
import math

input = sys.stdin.readline

x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
def minho(p):
    return [x1 + (x2 - x1) * (p/100), y1 + (y2 - y1) * (p/100)]

def kangho(p):
    return [x3 + (x4 - x3) * (p/100), y3 + (y4 - y3) * (p/100)]


fp = 0
lp = 100

length =  math.sqrt(pow(10000, 2) + pow(10000, 2))

while(lp-fp >= 1e-7):
    k1 = (fp*2 + lp)/3
    k2 = (fp + lp*2)/3
    
    m_k1 = minho(k1)
    m_k2 = minho(k2)

    k_k1 = kangho(k1)
    k_k2 = kangho(k2)

    #k1 에서의 민호와 강호의 거리
    dist_k1 = math.sqrt(pow(m_k1[0] - k_k1[0],2) + pow(m_k1[1] - k_k1[1],2))
    #k2 에서의 민호와 강호의 거리
    dist_k2 = math.sqrt(pow(m_k2[0] - k_k2[0],2) + pow(m_k2[1] - k_k2[1],2))
    

    length = min(length, min(dist_k1, dist_k2))
    
    if(dist_k1 >= dist_k2):
        fp = k1
    else:
        lp = k2
print('%.10f' %length)
