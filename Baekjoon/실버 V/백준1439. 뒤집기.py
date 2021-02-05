import sys
sys.stdin = open('백준1439. 뒤집기.txt', 'r')

S = input()
compare = S[0]
reduce = compare

for i in range(1, len(S)):
    if compare == S[i]:
        continue
    else:
        reduce += S[i]
        compare = S[i]
cnt_one, cnt_zero = 0, 0

for r in reduce:
    if r == '1':
        cnt_one += 1
    else:
        cnt_zero += 1

print(min(cnt_one, cnt_zero))