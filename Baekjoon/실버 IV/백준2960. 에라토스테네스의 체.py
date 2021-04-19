import sys
sys.stdin = open('백준2960. 에라토스테네스의 체.txt', 'r')
N, K = map(int, input().split())
check = [0] * (N+1)
answer = 2
num = 2
while K:
    for i in range(num, N+1, num):
        if not check[i]:
            check[i] = 1
            K -= 1
        if K == 0:
            answer = i
            break
    num += 1
print(answer)