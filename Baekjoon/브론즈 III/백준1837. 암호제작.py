import sys
sys.stdin = open('백준1837. 암호제작.txt', 'r')
P, K = map(int, input().split())
check = [0] * K
find = 0
for num in range(2, K):
    if not check[num]:
        for i in range(num, K, num):
            check[i] = 1
            if not P % num:
                find = num
                break
if find:
    other = P // find
    print("BAD {}".format(min(find, other)))
else:
    print("GOOD")