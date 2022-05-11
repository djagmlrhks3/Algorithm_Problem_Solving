import sys
sys.stdin = open('백준17427. 약수의 합 2.txt', 'r')
N = int(input())
answer = 0
for i in range(1, N+1):
    answer += (N//i) * i
print(answer)
