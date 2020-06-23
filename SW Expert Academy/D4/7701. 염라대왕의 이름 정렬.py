import sys
sys.stdin = open('7701. 염라대왕의 이름 정렬.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    names = set()
    for n in range(N):
        names.add(input())
    names = list(names)
    test = list()
    # print(names)
    for i in names:
        test.append((len(i),i))
    test.sort()
    print('#{}'.format(tc+1))
    for i in test:
        print(i[1])


