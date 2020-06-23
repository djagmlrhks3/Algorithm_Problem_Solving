import sys
sys.stdin = open('1234. 비밀번호.txt','r')

for tc in range(10):
    n, pw = input().split()
    empty = list()
    empty.append('')
    for i in range(int(n)):
        if empty[-1] != pw[i]:
            empty.append(pw[i])
        else:
            empty.pop(-1)
    result = ''
    for i in range(1,len(empty)):
        result += empty[i]
    print('#{} {}'.format(tc+1,result))