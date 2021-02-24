from collections import deque
import sys
sys.stdin=open("백준5430. AC.txt","r")

for _ in range(int(input())):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    if n:
        li = deque(list(map(int, input()[1:-1].split(','))))
    else:
        trash = input()
        li = []
    isReverse = False
    isError = False
    for order in p:
        if order == "R":
            isReverse = not isReverse
        else:
            if li:
                if isReverse:
                    li.pop()
                else:
                    li.popleft()
            else:
                isError = True
                break
    if isError:
        print("error")
    else:
        if isReverse: li = list(li)[::-1]
        else: li = list(li)
        print('[' + ','.join(map(str, li)) + ']')