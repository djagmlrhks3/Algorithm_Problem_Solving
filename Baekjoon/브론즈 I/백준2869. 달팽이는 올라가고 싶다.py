import sys
sys.stdin = open('백준2869. 달팽이는 올라가고 싶다.txt', 'r')

A, B, V = map(int, input().split())
snail, cnt = (A-B) * (V // (A-B) - A), V // (A-B) - A
while True:
    cnt += 1
    snail += A
    if snail >= V:
        break
    snail -= B
print(cnt)
