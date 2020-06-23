import sys
sys.stdin = open('5642. [Professional] 합.txt','r')


T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int,input().split()))

    for i in range(len(numbers)):
        maximum = 0
        flag = True
        s = i
        start = numbers[i]
        while s!=len(numbers)-1 :
            if numbers[s+1] >= 0:
                if numbers[s+1] + numbers[s+2] >=0 and numbers[s+2]>=0:
                    start += numbers[s+1] + numbers[s+2]
                    s += 2
                else:
                    start += numbers[s+1]
                    s += 1
            else:
                break
        print(start)
        if start > maximum:
            maximum = start
    print(maximum)
