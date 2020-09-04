import sys
sys.stdin = open('1206. View.txt', 'r')

def check(i):
    now = buildings[i]
    con1 = now - buildings[i - 2]
    con2 = now - buildings[i - 1]
    con3 = now - buildings[i + 1]
    con4 = now - buildings[i + 2]
    return min(con1, con2, con3, con4) if con1 > 0 and con2 > 0 and con3 > 0 and con4 > 0 else 0

for tc in range(10):
    L = int(input())
    buildings = list(map(int, input().split()))
    res = 0
    for i in range(2, L - 2):
        res += check(i)
    print('#{} {}'.format(tc + 1, res))