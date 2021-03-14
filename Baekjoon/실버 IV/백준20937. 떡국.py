import sys
sys.stdin = open('백준20937. 떡국.txt', 'r')

N = int(input())
bowls = list(map(int, sys.stdin.readline().split()))
bowls.sort(reverse=True)
cnt = [0] * (max(bowls)+1)
for num in bowls:
    cnt[num] += 1
print(max(cnt))