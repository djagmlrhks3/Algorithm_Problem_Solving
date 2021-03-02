import sys
sys.stdin = open('백준10972. 다음 순열.txt', 'r')

def next_permuation(numbers):
    k = N - 2
    flag = False
    while k >= 0:
        if numbers[k] < numbers[k+1]:
            for idx in range(N-1, k, -1):
                if numbers[k] < numbers[idx]:
                    pick = idx
                    flag = True
                    break
        if flag: break
        k -= 1
    if flag:
        numbers[k], numbers[pick] = numbers[pick], numbers[k]
        return ' '.join(map(str, numbers[:k+1] + numbers[k+1:][::-1]))
    else:
        return -1
N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
print(next_permuation(numbers))
