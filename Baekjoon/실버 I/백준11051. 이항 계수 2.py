import sys
sys.stdin = open('백준11051. 이항 계수 2.txt', 'r')

N, K = map(int, input().split())
answer = 1
for num in range(N, N-K, -1):
    answer *= num

for num in range(K, 1, -1):
    answer //= num

print(answer % 10007)