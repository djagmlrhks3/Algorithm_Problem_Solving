import sys
sys.stdin = open('백준11729. 하노이 탑 이동 순서.txt', 'r')

N = int(input())

answer = []
def hanoi(n, start, end, assist):
    if n == 1:
        answer.append((start, end))
        return
    hanoi(n-1, start, assist, end)
    answer.append((start, end))
    hanoi(n-1, assist, end, start)

hanoi(N, 1, 3, 2)

print(len(answer))
for s, e in answer:
    print(s, e)