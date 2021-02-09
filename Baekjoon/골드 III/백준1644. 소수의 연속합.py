import sys
sys.stdin = open('백준1644. 소수의 연속합.txt', 'r')

def check(num): # 1 ~ N까지 소수 찾기
    global N
    for idx in range(2*num, N+1, num):
        numbers[idx] = 0

N = int(input())
numbers = [0, 0] + [1] * (N-1)

for num in range(1, len(numbers)):
    if numbers[num]:
        check(num)

candidates = [] # N까지 소수를 담을 배열

for idx in range(len(numbers)): # 소수를 candidates 배열에 담기
    if numbers[idx]:
        candidates.append(idx)

left, right = 0, 1 # 투 포인터
answer = 0 # 정답을 담을 변수

while left <= right and right <= len(candidates):
    temp = sum(candidates[left:right])
    if temp == N:
        answer += 1
        right += 1
    elif temp < N:
        right += 1
    else:
        left += 1
print(answer)