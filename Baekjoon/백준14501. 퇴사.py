import sys
sys.stdin = open('백준14501. 퇴사.txt', 'r')

N = int(input())
candidates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
def earn(day, money):
    global answer
    answer = max(answer, money)
    if day >= N: return

    if day + candidates[day][0] <= N:
        earn(day + candidates[day][0], money + candidates[day][1])
        earn(day + 1, money)
    else:
        earn(day + 1, money)
    return

earn(0, 0)
print(answer)