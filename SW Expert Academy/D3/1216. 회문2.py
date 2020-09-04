import sys
sys.stdin = open('1216. 회문2.txt', 'r')

def check(square):
    for i in range(100, 1, -1): # 회문 길이
        for j in range(100): # 행(아래로)
            for z in range(100 - i + 1): # 시작, 끝
                word = square[j][z:100-(100-i)+z]
                if word == word[::-1]:
                    return len(word)


for tc in range(10):
    N = int(input())
    origin = [input() for _ in range(100)]
    reverse = ['' * 100 for _ in range(100)]
    for o in origin:
        for i in range(100):
            reverse[i] += o[i]

    first = check(origin)
    second = check(reverse)
    print('#{} {}'.format(N, max(first, second)))