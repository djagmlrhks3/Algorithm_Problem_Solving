import sys
sys.stdin = open('백준13458. 시험 감독.txt', 'r')

N = int(input())
students = list(map(int, sys.stdin.readline().split()))
B, C = map(int, input().split())

answer = 0
for student in students:
    student -= B
    answer += 1
    if student > 0:
        if student % C:
            answer += (student//C + 1)
        else:
            answer += (student//C)

print(answer)

