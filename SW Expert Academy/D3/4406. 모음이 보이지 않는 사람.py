import sys
sys.stdin = open('4406. 모음이 보이지 않는 사람.txt','r')

T = int(input())
for tc in range(T):
    vowels= 'aeiou'
    words = input()
    result = ''
    for i in range(len(words)):
        if words[i] not in vowels:
            result += words[i]
    print('#{} {}'.format(tc+1,result))