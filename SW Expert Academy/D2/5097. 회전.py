import sys, collections
sys.stdin = open('5097. 회전.txt','r')

# T = int(input())
# for tc in range(T):
#     N, M = map(int,input().split())
#     input_data = list(map(int,input().split()))
#     result = input_data[M%N]
#     print('#{} {}'.format(tc+1,result))
"""
import collections 사용
"""
# T = int(input())
# for tc in range(T):
#     N, M = map(int,input().split())
#     input_data = list(map(int,input().split()))
    # q = _collections.deque()
    # for i in input_data:
    #     q.append(i)
    # for i in range(M):
    #     P = q.popleft()
    #     q.append(P)
    # print('#{} {}'.format(tc+1,q[0]))

# T = int(input())
# for tc in range(T):
#     N, M = map(int,input().split())
#     input_data = list(map(int,input().split()))
#     for i in range(M):
#         P = input_data.pop(0)
#         input_data.append(P)
#     print('#{} {}'.format(tc+1,input_data[0]))

def enQueue(item):
    global rear
    if isFull(): print('다찼음')
    else:
        rear += 1
        Q.append(item)
def deQueue():
    global front
    if isEmpty(): print('비었음')
    else:
        front += 1
        return Q[front]
def isEmpty():
    if front == rear:return True
    else: return False
def isFull():
    if rear == 2:
        return True
    else:
        return False

input_data = [1,2,3]
front = rear = -1
Q = list()
for i in input_data:
    enQueue(i)
for i in range(3):
    print(deQueue())










