import sys
sys.stdin = open('백준20540. 연결이의 이상형.txt', 'r')

all_mbti = 'EISNTFJP'
MBTI = input()
answer = ''
for word in MBTI:
    idx = all_mbti.index(word)
    if idx % 2:
        idx -= 1
    else:
        idx += 1
    answer += all_mbti[idx]
print(answer)
