import sys
sys.stdin = open('백준1550. 16진수.txt', 'r')
alpha = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
given = input()[::-1]
answer = 0
for idx in range(len(given)):
    if given[idx].isalpha():
        answer += (16 ** idx) * alpha[given[idx]]
    else:
        answer += (16 ** idx) * int(given[idx])
print(answer)


