import sys
sys.stdin = open('백준1789. 수들의 합.txt', 'r')

S = int(input())
num = 1
while (num * (num + 1)) // 2 <= S:
    num += 1

print(num-1)