import sys
sys.stdin = open('백준11557. Yangjojang of The Year.txt', 'r')

for _ in range(int(input())):
    candidates = dict()
    for _ in range(int(input())):
        school, num = sys.stdin.readline().split()
        if school not in candidates.keys():
            candidates[school] = int(num)
        else:
            candidates[school] += int(num)
    print(sorted(candidates.items(), key=lambda x:[-x[1]])[0][0])