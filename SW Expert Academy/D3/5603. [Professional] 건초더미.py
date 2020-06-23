import sys
sys.stdin = open('5603. [Professional] 건초더미.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    guncho = list()
    for n in range(N):
        guncho.append(int(input()))
    average = int(sum(guncho)/N)
    diff = 0
    for i in guncho:
        if i > average:
            diff += i-average
    print('#{} {}'.format(tc+1,diff))