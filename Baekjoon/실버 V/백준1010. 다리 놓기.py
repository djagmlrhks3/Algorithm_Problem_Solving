import sys
sys.stdin = open('백준1010. 다리 놓기.txt', 'r')

T = int(input())
for _ in range(T):
    left, right = map(int, input().split())
    answer = 1
    for num in range(right, right-left, -1):
        answer *= num
    for num in range(left, 1, -1):
        answer //= num
    print(answer)