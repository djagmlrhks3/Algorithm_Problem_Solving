import sys
from collections import deque
sys.stdin = open('백준14226. 이모티콘.txt', 'r')
S = int(input())
DP = dict()
DP[(1, 0)] = 0
queue = deque([(1, 0)])
time = 1
while queue:
    emo, clip = queue.popleft()
    if emo == S:
        print(DP[(emo, clip)])
        break
    if emo + clip > 1000: continue
    if (emo+clip, clip) not in DP.keys(): # 붙여넣기
        DP[(emo+clip, clip)] = DP[(emo, clip)] + 1
        queue.append((emo+clip, clip))
    if emo-1 >= 2 and (emo-1, clip) not in DP.keys(): # 삭제
        DP[(emo-1, clip)] = DP[(emo, clip)] + 1
        queue.append((emo-1, clip))
    if (emo, emo) not in DP.keys(): # 복사
        DP[(emo, emo)] = DP[(emo, clip)] + 1
        queue.append((emo, emo))