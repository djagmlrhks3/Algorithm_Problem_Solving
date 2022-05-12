import sys
sys.stdin = open('백준21734. SMUPC의 등장.txt', 'r')

S = input()
for w in S:
    total = 0
    for num in str(ord(w)):
        total += int(num)
    print(w * total)
