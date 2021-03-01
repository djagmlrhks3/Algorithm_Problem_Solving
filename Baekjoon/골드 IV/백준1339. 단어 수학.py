import sys
sys.stdin = open('백준1339. 단어 수학.txt', 'r')

N = int(input())
used = [False] * 10 # 숫자 사용 여부
words = [sys.stdin.readline().rstrip() for _ in range(N)]
alphabets = set()
for word in words:
    alphabets = alphabets | set(word)
alphabets = list(alphabets)

weight = {}
for alpha in alphabets:
    for word in words:
        temp = ''
        for w in word:
            if w == alpha: temp += '1'
            else: temp += '0'
        if alpha not in weight.keys():  weight[alpha] = int(temp)
        else: weight[alpha] += int(temp)
weight = sorted(weight.items(), key=lambda x:[-x[1]])

result = {}
for alpha, value in weight:
    for idx in range(10):
        if not used[idx]:
            result[alpha] = 10-idx-1
            used[idx] = True
            break

answer = 0
for word in words:
    temp = ''
    for alpha in word:
        temp += str(result[alpha])
    answer += int(temp)
print(answer)