import sys
sys.stdin = open('2117. 홈 방범 서비스.txt','r')
"""
도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M
K * K + (K - 1) * (K - 1)

for k in range(K):
    
"""
T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    cities = [list(map(int,input().split())) for _ in range(N)]

    
    # for i in cities:
    #     print(i)