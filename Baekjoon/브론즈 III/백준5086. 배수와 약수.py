import sys
sys.stdin = open('백준5086. 배수의 약수.txt', 'r')

while True:
    A, B = map(int, input().split())
    if not A and not B: break
    if not B % A and B > A:
        print("factor")
    elif not A % B and A >= B:
        print("multiple")
    else:
        print("neither")