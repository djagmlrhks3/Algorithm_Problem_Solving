import sys
sys.stdin = open('백준15953. 상금 헌터.txt', 'r')
test_2017 = {1:500, 3:300, 6:200, 10:50, 15:30, 21:10}
test_2018 = {1:512, 3:256, 7:128, 15:64, 31:32}
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    reward = 0
    if a and a <= 21:
        for key in test_2017.keys():
            if a <= key:
                reward += test_2017[key]
                break
    if b and b <= 31:
        for key in test_2018.keys():
            if b <= key:
                reward += test_2018[key]
                break
    print(reward * 10**4)