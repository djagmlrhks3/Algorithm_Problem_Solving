import sys
from collections import Counter
sys.stdin = open('백준2108. 통계학.txt', 'r')

N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()
cnt = sorted(Counter(numbers).most_common(), key=lambda x:(-x[1]))

print(round(sum(numbers)/N)) # 산술평균
print(numbers[len(numbers)//2]) # 중앙값
print(cnt[1][0]) if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else print(cnt[0][0]) # 최빈값 - 다수일 경우 2번째로 작은 값 출력
print(numbers[-1] - numbers[0]) # 범위(최대값 - 최소값)