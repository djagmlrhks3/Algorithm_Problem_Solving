import sys
sys.stdin = open('백준17425. 약수의 합.txt', 'r')

T = int(input())
candidates = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
maximum = max(candidates)
results = [i for i in range(maximum+1)]
for i in range(1, maximum+1):
    for j in range(i*2, maximum+1, i):
        results[j] += i
    results[i] += results[i-1]
for num in candidates:
    print(results[num])