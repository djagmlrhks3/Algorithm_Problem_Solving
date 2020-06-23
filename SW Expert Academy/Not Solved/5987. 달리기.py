import sys
sys.stdin=open('5987. 달리기.txt','r')

def chk(n,li):
    global count
    if n == N and li not in stack:
        count += 1
        return
    else:



T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    sample = list()
    for m in range(M):
        empty=list(map(int,input().split()))
        if m == 0:
            sample.append(empty)
        else:
            for i in sample:
                if i[-1] == empty[0]:
                    i.append(empty[1])
                else:
                    sample.append(empty)
                    break
    stack = list()
    human = [ i for _ in range(1,N+1)]
    count = 0
    for i in sample:
        chk(len(i),i)
    print(sample)