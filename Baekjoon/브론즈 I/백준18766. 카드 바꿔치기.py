import sys
sys.stdin = open('백준18766. 카드 바꿔치기.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    before = sys.stdin.readline().split()
    after = sys.stdin.readline().split()
    before.sort()
    after.sort()
    for idx in range(n):
        if before[idx] != after[idx]:
            print("CHEATER")
            break
    else:
        print("NOT CHEATER")