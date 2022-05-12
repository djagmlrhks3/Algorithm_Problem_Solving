import sys
sys.stdin = open('백준21603. K 2K 게임.txt', 'r')

N, K = map(int, input().split())
compare = [K%10, (2*K)%10]
numbers = []
for i in range(1, N+1):
    if i % 10 not in compare:
        numbers.append(i)
print(len(numbers))
print(' '.join(map(str, numbers)))