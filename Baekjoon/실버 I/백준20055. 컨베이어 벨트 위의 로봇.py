import sys
sys.stdin = open('백준20055. 컨베이어 벨트 위의 로봇.txt', 'r')
from collections import deque
N, K = map(int, input().split())
convey = deque(list(map(int, sys.stdin.readline().split())))
robot = deque([0] * N)

answer = 0
while convey.count(0) < K:
    convey.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for idx in range(N-2, -1, -1):
            if robot[idx] and not robot[idx+1] and convey[idx+1]:
                convey[idx+1] -= 1
                robot[idx+1], robot[idx] = 1, 0
        robot[-1] = 0

    if not robot[0] and convey[0]:
        robot[0] = 1
        convey[0] -= 1

    answer += 1

print(answer)
