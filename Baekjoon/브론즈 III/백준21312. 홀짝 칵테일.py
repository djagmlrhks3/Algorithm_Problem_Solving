import sys
sys.stdin = open('백준21312. 홀짝 칵테일.txt', 'r')

answer, odd = 1, False
cocktail = list(map(int, input().split()))
for num in cocktail:
    if num % 2:
        answer *= num
        odd = True
print(answer) if odd else print(cocktail[0] * cocktail[1] * cocktail[2])