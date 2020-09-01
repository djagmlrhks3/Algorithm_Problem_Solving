import sys
sys.stdin = open('1238. Contact.txt', 'r')

from collections import deque

def bfs(n):
    global maximum
    queue = deque([n])
    step = [0] * (maximum+1)
    step[n] = 0
    while(queue):
        num = queue.popleft()
        if num in network.keys():
            for i in network[num]:
                if not step[i]:
                    queue.append(i)
                    step[i] = step[num] + 1
    return maximum - step[::-1].index(max(step))

for tc in range(10):
    N, S = map(int, input().split())
    nodes = list(map(int, input().split()))
    maximum = max(nodes)
    network = dict()
    for i in range(0, len(nodes), 2):
        if nodes[i] not in list(network.keys()):
            network[nodes[i]] = [nodes[i+1]]
        else:
            network[nodes[i]].append(nodes[i+1])
    print('#{} {}'.format(tc+1, bfs(S)))
