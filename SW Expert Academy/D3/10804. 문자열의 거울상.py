import sys
sys.stdin = open('10804. 문자열의 거울상.txt', 'r')

T = int(input())
for tc in range(T):
    words = input()
    res = ''
    for i in range(len(words)-1, -1, -1):
        if words[i] == 'b':
            res += 'd'
        elif words[i] == 'd':
            res += 'b'
        elif words[i] == 'p':
            res += 'q'
        else:
            res += 'p'
    print('#{} {}'.format(tc+1, res))