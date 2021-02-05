import sys
sys.stdin = open('백준14888. 연산자 끼워넣기.txt','r')

def chk(number,idx):
    global minimum, maximum
    if idx == N-1:
        if number not in candidate:
            candidate.append(number)
    else:
        if order[0] > 0: #+
            order[0] -= 1
            chk(number+numbers[idx + 1], idx + 1)
            order[0] += 1
        if order[1] > 0: #-
            order[1] -= 1
            chk(number - numbers[idx + 1], idx + 1)
            order[1] += 1
        if order[2] > 0: #*
            order[2] -= 1
            chk(number * numbers[idx + 1], idx + 1)
            order[2] += 1
        if order[3] > 0: #/
            order[3] -= 1
            chk(int(number / numbers[idx + 1]), idx + 1)
            order[3] += 1
N = int(input())
numbers = list(map(int,input().split()))
order = list(map(int,input().split()))

candidate = list()
chk(numbers[0],0)
print(max(candidate))
print(min(candidate))
