import sys
sys.stdin = open('10912. 외로운 문자.txt', 'r')

T = int(input())
for tc in range(T):
    words = input()
    used = []
    candidates = []
    for i in words:
        if i not in used:
            used.append(i)
            if words.count(i)%2:
                candidates.append(i)
    candidates.sort()
    res = 'Good' if not len(candidates) else ''.join(candidates)
    print('#{} {}'.format(tc+1, res))