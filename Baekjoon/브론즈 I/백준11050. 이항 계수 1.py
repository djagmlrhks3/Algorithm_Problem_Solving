import sys
sys.stdin = open('백준11050. 이항 계수 1.txt', 'r')

N, K = map(int, input().split())
answer = 1
for num in range(N, N-K, -1):
    answer *= num

for num in range(K, 1, -1):
    answer //= num

print(answer)