import sys
sys.stdin = open('백준3649. 로봇 프로젝트.txt', 'r')

while True:
    try:
        x = int(input())
        n = int(input())
        lego = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
        lego.sort()
        left, right = 0, n-1
        while left < right:
            if (lego[left] + lego[right]) == x * 10000000:
                break
            elif (lego[left] + lego[right]) > x * 10000000:
                right -= 1
            else:
                left += 1
        if left < right:
            print('yes {} {}'.format(lego[left], lego[right]))
        else:
            print('danger')
    except:
        break