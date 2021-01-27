import sys
sys.stdin = open('백준1525. 퍼즐.txt', 'r')
from collections import deque

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs():
    while queue:
        p = queue.popleft()
        if p == '123456780': # '123456789' - 정리된 상태가 되면 종료
            return step[p]
        zero = p.find('0') # '0'의 위치를 찾는다.
        r, c = zero // 3, zero % 3 # '0'의 인덱스를 이용해 행, 열 좌표를 계산한다.
        for idx in range(4): # 4방향 탐색을 통해서 3x3 배열 밖에 벗어나지 않는지 확인한다.
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < 3 and 0 <= nc < 3:
                p_list = list(p) # string → list
                p_list[zero], p_list[nr*3+nc] = p_list[nr*3+nc], p_list[zero] # 원소를 바꾼다.
                new_p = ''.join(p_list) # list → string
                if new_p not in step.keys(): # 새로운 퍼즐(new_p)이 step의 key에 없다면 추가한다.(이동횟수+1)
                    step[new_p] = step[p] + 1
                    queue.append(new_p)
    return -1 # 찾지못하면 -1 return

inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
puzzle = '' # inputs의 3x3 배열을 한줄로 나열

for r in range(3):
    row = ''
    for c in range(3):
        row += str(inputs[r][c])
    puzzle += row

step = {puzzle : 0} # dictionary를 이용하여 "퍼즐:이동횟수" 형식으로 key-value를 넣는다.
queue = deque([puzzle]) # queue
print(bfs())