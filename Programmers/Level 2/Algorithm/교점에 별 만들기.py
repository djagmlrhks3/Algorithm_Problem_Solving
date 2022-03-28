from itertools import combinations


def solution(line):
    candidates = []
    for li in combinations(range(len(line)), 2):
        idx1, idx2 = li[0], li[1]
        A, B, E = line[idx1]
        C, D, F = line[idx2]
        if A * D - B * C:
            x = (B * F - E * D) / (A * D - B * C)
            y = (E * C - A * F) / (A * D - B * C)
            if x == int(x) and y == int(y):
                candidates.append((int(x), int(y)))
    width = sorted(candidates, key=lambda x: x[0])
    x1, x2 = width[0][0], width[-1][0]

    height = sorted(candidates, key=lambda x: x[1])
    y1, y2 = height[0][1], height[-1][1]

    w, h = x2 - x1 + 1, y2 - y1 + 1
    star = [['.'] * w for _ in range(h)]
    for x, y in candidates:
        star[abs(y2 - y)][abs(x1 - x)] = '*'
    return [''.join(li) for li in star]