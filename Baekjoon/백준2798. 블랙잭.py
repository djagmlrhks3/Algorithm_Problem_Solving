import sys
from itertools import combinations
sys.stdin = open('백준2798. 블랙잭.txt', 'r')

"""
조합(Combinations) 이용
"""
N, M = map(int, input().split())
answer = 0
for li in combinations(list(map(int, sys.stdin.readline().split())), 3):
    if sum(li) <= M:
        answer = max(answer, sum(li))
print(answer)

"""
삼중 for문 이용
"""
# N, M = map(int, input().split())
# answer = 0
#
# numbers = list(map(int, sys.stdin.readline().split()))
# for first in range(len(numbers)):
#     for second in range(1, len(numbers)):
#         if first == second: continue
#         if numbers[first] + numbers[second] >= M:continue
#         for third in range(2, len(numbers)):
#             if first == third or second == third:continue
#             if numbers[first] + numbers[second] + numbers[third] <= M:
#                 answer = max(answer, numbers[first] + numbers[second] + numbers[third])
# print(answer)