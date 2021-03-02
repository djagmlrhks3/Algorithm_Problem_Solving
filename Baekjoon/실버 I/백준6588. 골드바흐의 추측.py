import sys
sys.stdin = open('백준6588. 골드바흐의 추측.txt', 'r')

check = [True] * 1000001

for num in range(2, 1000001):
    if check[num]:
        for idx in range(num*2, 1000001, num):
            check[idx] = False
while True:
    n = int(sys.stdin.readline().rstrip())
    if not n: break
    a, b = 2, n
    while a <= b:
        if a + b == n: break
        elif a + b > n:
            while True:
                b -= 1
                if check[b]:
                    break
        else:
            while True:
                a += 1
                if check[a]:
                    break
    if a <= b: print('{} = {} + {}'.format(n, a, b))
    else: print("Goldbach's conjecture is wrong.")