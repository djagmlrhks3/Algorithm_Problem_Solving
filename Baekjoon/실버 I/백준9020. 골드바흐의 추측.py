import sys
sys.stdin = open('백준9020. 골드바흐의 추측.txt', 'r')

candidates = [False] * 2 + [True] * 9999


for num in range(2, len(candidates)//2):
    if candidates[num]:
        for idx in range(2*num, len(candidates), num):
            candidates[idx] = False

T = int(input())
for _ in range(T):
    n = int(input())
    one = n//2
    while True:
        the_other = n - one
        if candidates[one] and candidates[the_other]:
            print(one, the_other)
            break
        one -= 1

