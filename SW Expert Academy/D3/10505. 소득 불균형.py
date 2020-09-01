import sys
sys.stdin = open('10505. 소득 불균형.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    res = 0
    numbers = list(map(int, input().split()))
    avg = sum(numbers) / N
    for num in numbers:
        if num <= avg:
            res += 1
    print('#{} {}'.format(tc+1, res))