import sys
sys.stdin = open('백준1406. 에디터.txt', 'r')
left = list(''.join(map(str, sys.stdin.readline().rstrip())))
right = []
M = int(input())
for _ in range(M):
    order, *word = sys.stdin.readline().split()
    if order == 'L' and left:
        right.append(left.pop())
    elif order == 'D' and right:
        left.append(right.pop())
    elif order == 'B' and left:
        left.pop()
    elif order == 'P':
        left.append(word[0])
print(''.join(map(str, left+right[::-1])))