d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
def check(p, place):
    visited = [[0] * 5 for _ in range(5)]
    people = [p]
    while people:
        r, c, depth = people.pop()
        visited[r][c] = 1
        if depth > 2: continue
        for i in range(4):
            nr = r + d[i][0]
            nc = c + d[i][1]
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
               if place[nr][nc] == 'O':
                   people.append((nr, nc, depth+1))
                   visited[nr][nc] = 1
               elif place[nr][nc] == 'P' and depth+1 < 3:
                   return False
    return True

def solution(places):
    answer = []
    for place in places:
        people = []
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    people.append((r, c, 0))

        for p in people:
            if not check(p, place):
                answer.append(0)
                break
        else:
            answer.append(1)
    return answer
