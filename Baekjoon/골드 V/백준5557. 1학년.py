import sys
sys.stdin = open('백준5557. 1학년.txt', 'r')

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
want = numbers.pop()
DP_before = [0] * 21
DP_before[numbers[0]] = 1

DP_after = [0] * 21
for i in range(1, len(numbers)):
    for j in range(len(DP_before)):
        if DP_before[j]:
            if j + numbers[i] <= 20:
                DP_after[j+numbers[i]] += DP_before[j]
            if j - numbers[i] >= 0:
                DP_after[j-numbers[i]] += DP_before[j]
    DP_before = DP_after
    DP_after = [0] * 21
print(DP_before[want])