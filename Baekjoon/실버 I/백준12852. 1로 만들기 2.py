import sys
from collections import deque
sys.stdin = open('백준12852. 1로 만들기 2.txt', 'r')

def cal(before, after, string):
    if after == 0: return
    check[after] = check[before]+1
    queue.append((after, string+' '+str(after)))

N = int(input())
queue = deque([(N, str(N))])
check = [0] * 1000001
check[N] = 0
while True:
    num, string = queue.popleft()
    if num == 1:
        print(check[1])
        print(string)
        break
    if num%3 == 0 and not check[num//3]:
        cal(num, num//3, string)
    if num%2 == 0 and not check[num//2]:
        cal(num, num//2, string)
    if 0 < num-1 and not check[num-1]:
        cal(num, num-1, string)