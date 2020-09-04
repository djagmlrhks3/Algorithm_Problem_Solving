import sys
sys.stdin = open('1208. Flatten.txt', 'r')

for tc in range(10):
    dump = int(input())
    wall = list(map(int, input().split()))
    
    for i in range(dump):
        wall[wall.index(max(wall))] -= 1
        wall[wall.index(min(wall))] += 1
    print('#{} {}'.format(tc+1, max(wall) - min(wall)))