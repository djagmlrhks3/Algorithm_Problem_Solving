import sys
sys.stdin = open('백준20528. 끝말잇기.txt', 'r')

N = int(input())
words = sys.stdin.readline().split()
compare = words[0][0]
for word in words:
    if word[0] != compare:
        print(0)
        break
else:
    print(1)