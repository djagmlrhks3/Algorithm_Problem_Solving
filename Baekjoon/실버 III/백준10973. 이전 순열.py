import sys
sys.stdin = open('백준10973. 이전 순열.txt', 'r')

def find_prev(numbers):
    k = N-2
    flag = False
    while k >= 0:
        if numbers[k] > numbers[k+1]: # 앞에 큰 값을 찾는다.
            for idx in range(N-1, k, -1):
                if numbers[k] > numbers[idx]:
                    pick = idx
                    flag = True
                    break
        if flag: break
        k -= 1
    if flag:
        numbers[k], numbers[pick] = numbers[pick], numbers[k]
        res = numbers[:k+1] + sorted(numbers[k+1:])[::-1]
        return ' '.join(map(str, res))
    return -1

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
print(find_prev(numbers))