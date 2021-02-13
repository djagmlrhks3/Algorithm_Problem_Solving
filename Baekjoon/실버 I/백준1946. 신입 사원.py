import sys
sys.stdin = open('백준1946. 신입 사원.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    scores = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    interview_scores = sorted(scores, key=lambda x:(x[0]))
    answer = 1
    compare = interview_scores[0][1]
    for idx in range(1, N):
        if interview_scores[idx][1] <= compare:
            compare = min(interview_scores[idx][1], compare)
            answer += 1
    print(answer)