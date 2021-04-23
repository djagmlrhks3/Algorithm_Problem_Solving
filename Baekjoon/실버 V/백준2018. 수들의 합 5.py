import sys
sys.stdin = open('백준2018. 수들의 합 5.txt', 'r')

N = int(input())
answer = 1
if N > 2:
    numbers = [i for i in range(1, N + 1)]
    l, r = 0, 1
    temp = numbers[l] + numbers[r]
    while l < r:
        if temp > N:
            temp -= numbers[l]
            l += 1
        else:
            if temp == N:
                answer += 1
            r += 1
            if r == N: break
            temp += numbers[r]
print(answer)