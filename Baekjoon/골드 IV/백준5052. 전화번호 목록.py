def check():
    for idx in range(n-1):
        if phones[idx] == phones[idx+1][:len(phones[idx])]:
            print("NO")
            return
    print("YES")

import sys
sys.stdin = open('백준5052. 전화번호 목록.txt', 'r')
for _ in range(int(input())):
    n = int(input())
    phones = [sys.stdin.readline().rstrip() for _ in range(n)]
    phones.sort()
    check()