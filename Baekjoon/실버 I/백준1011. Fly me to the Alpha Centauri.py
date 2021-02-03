import sys
sys.stdin = open('백준1011. Fly me to the Alpha Centauri.txt', 'r')

"""
문제의 핵심은 목적지 단계에서는 1만큼 이동해야 한다.
즉, 특정 지점에서 에너지 소모를 얼만큼 해야 최소 작동 횟수를 구할 수 있는지가 핵심!
"""
def calculate(n):
    return n * (n+1) // 2

T = int(input())
for tc in range(T):
    routes = [1]
    x, y = map(int, input().split())
    start, end, move, cnt = 1, y-x, 1, 1 # 출발지점, 목적지, (현재)에너지 소모, 이동 장치 작동 횟수
    while start != end: # 목적지에 도착할 때까지 반복
        for v in range(move+1, move-2, -1):
            if v > 0: # 1이상의 움직임만 의미가 있다.
                if start + calculate(v) <= end:
                    start += v
                    move = v
                    routes.append(v)
                    cnt += 1
                    break
    print(cnt)



