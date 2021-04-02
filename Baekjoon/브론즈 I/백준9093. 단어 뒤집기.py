import sys
sys.stdin = open('백준9093. 단어 뒤집기.txt', 'r')

for _ in range(int(input())):
    sentence = sys.stdin.readline().split()
    for idx in range(len(sentence)):
        sentence[idx] = sentence[idx][::-1]
    print(' '.join(sentence))