import sys
sys.stdin = open('백준5585. 거스름돈.txt', 'r')

given = int(input())
cost = 1000 - given
ex = [500, 100, 50, 10, 5, 1]
answer = 0
idx = 0
while cost:
    if cost // ex[idx]:
        answer += (cost // ex[idx])
        cost = cost % ex[idx]
    idx += 1
print(answer)