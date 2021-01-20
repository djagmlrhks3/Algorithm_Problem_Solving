import sys
from itertools import combinations
sys.stdin = open('백준15686. 치킨 배달.txt', 'r')

def distance(hr, hc, cr, cc):
    return abs(hr-cr) + abs(hc-cc)
N, M = map(int, sys.stdin.readline().split())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

house = []
chicken = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house.append((r, c))
        elif city[r][c] == 2:
            chicken.append((r, c))

answer = 0xffff
for combi in combinations(chicken, M):
    temp = 0 # M개의 치킨집을 골랐을 때 치킨거리를 담는 변수
    for h in house: # 모든 집에 대해서
        hr, hc = h
        dist = 0xffff
        for c in combi: # 각 치킨집까지의 거리를 계산
            cr, cc = c
            dist = min(dist, distance(hr, hc, cr, cc)) # 해당집에서 가장 가까운 치킨거리로 최신화
        temp += dist # temp에 dist 누적
        if temp >= answer: break # 중간단계에서 이전보다 큰 치킨거리가 나오면 break - 가지치기
    answer = min(answer, temp) # 모든 조합에서 가장 작은 치킨거리로 최신화

print(answer)
