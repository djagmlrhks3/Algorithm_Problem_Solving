import sys
sys.stdin = open('4698. 테네스의 특별한 소수.txt')
T = int(input())
for tc in range(T):
    D,A,B = map(int,input().split())
    sample = list()
    if A <= 2:
        sample.append(2)
    count = 0
    for i in range(A,B+1):
        for j in range(2,i):
            if i%j == 0 :
                count += 1
        if count == 1:
            sample.append(i)
    print(sample)