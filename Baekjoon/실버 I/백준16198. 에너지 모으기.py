import sys
sys.stdin = open('백준16198. 에너지 모으기.txt', 'r')

def recursive(li, total):
    global answer
    if len(li) == 3:
        total += li[0] * li[-1]
        answer = max(answer, total)
        return

    for idx in range(1, len(li)-1):
        recursive(li[:idx] + li[idx+1:],total + li[idx-1] * li[idx+1])


N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

answer = 0
recursive(numbers[:], 0)
print(answer)