import sys
sys.stdin = open('17136. 색종이 붙이기.txt', 'r')

def check(r, c, length, full):
    for i in range(length):
        full -= sum(papers[r+i][c:c+length])
    if full:
        return False
    else:
        return True

def recursive(one, cnt):
    global answer
    if not one:
        answer = min(answer, cnt)
        return
    if cnt >= answer:
        return
    if not sum(used):
        return
    for r in range(10):
        for c in range(10):
            if papers[r][c]:
                for length in range(5, 0, -1):
                    if used[length] and r+length <= 10 and c+length <= 10:
                        if check(r, c, length, length**2):
                            for i in range(r, r+length):
                                for j in range(c, c+length):
                                    papers[i][j] = 0
                            used[length] -= 1
                            recursive(one - length**2, cnt+1)
                            for i in range(r, r+length):
                                for j in range(c, c+length):
                                    papers[i][j] = 1
                            used[length] += 1
                return

papers = []
used = [0]+[5]*5
answer = 0xfffff
one = 0
for _ in range(10):
    paper = list(map(int, sys.stdin.readline().split()))
    one += sum(paper)
    papers.append(paper)
if not one:
    print(0)
else:
    recursive(one, 0)
    print(-1) if answer == 0xfffff else print(answer)
"""
1x1 ~ 5x5
"""