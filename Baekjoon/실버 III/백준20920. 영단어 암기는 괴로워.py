import sys
sys.stdin = open('백준20920. 영단어 암기는 괴로워.txt', 'r')

N, M = map(int, input().split())
words = dict()
for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) < M: continue
    if word not in words.keys(): words[word] = [1, len(word), word]
    else: words[word][0] += 1

words = sorted(words.values(), key=lambda x:[-x[0], -x[1], x[2]])
for word in words:
    print(word[2])