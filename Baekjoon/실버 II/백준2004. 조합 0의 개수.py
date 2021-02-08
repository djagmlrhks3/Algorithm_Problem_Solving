import sys
sys.stdin = open('백준2004. 조합 0의 개수.txt', 'r')

#num!에서 divnum 숫자의 개수를 파악하는 함수
def calculate(num, divnum):
    answer = 0
    while num:
        num //= divnum
        answer += num
    return answer

n, m = map(int, input().split())

print(min(calculate(n, 5) - calculate(n-m, 5) - calculate(m, 5), calculate(n, 2) - calculate(n-m, 2) - calculate(m, 2)))
