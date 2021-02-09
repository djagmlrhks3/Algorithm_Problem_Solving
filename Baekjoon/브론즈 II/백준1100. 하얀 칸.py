import sys
sys.stdin = open('백준1100. 하얀 칸.txt', 'r')

grid = [input() for _ in range(8)]

even = [0, 2, 4, 6]
odd = [1, 3, 5, 7]

answer = 0
for idx in range(len(grid)):
    if idx % 2:
        for col in odd:
            if grid[idx][col] == 'F':
                answer += 1

    else:
        for col in even:
            if grid[idx][col] == 'F':
                answer += 1

print(answer)