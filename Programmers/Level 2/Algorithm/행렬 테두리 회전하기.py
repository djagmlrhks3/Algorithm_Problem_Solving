def solution(rows, columns, queries):
    
    def rotate(r1, c1, r2, c2):
        save = matrix[r1][c1]
        mini = save
        #좌
        for r in range(r1, r2):
            matrix[r][c1] = matrix[r+1][c1]
            mini = min(mini, matrix[r][c1])
        #하
        for c in range(c1, c2):
            matrix[r2][c] = matrix[r2][c+1]
            mini = min(mini, matrix[r2][c]) 
        #우
        for r in range(r2, r1, -1):
            matrix[r][c2] = matrix[r-1][c2]
            mini = min(mini, matrix[r][c2])
        #상
        for c in range(c2, c1, -1):
            matrix[r1][c] = matrix[r1][c-1]
            mini = min(mini, matrix[r1][c])
        matrix[r1][c1+1] = save
        return mini
              
    matrix = [[0] * columns for _ in range(rows)]
    num = 1
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = num
            num += 1
    answer = []
    for r1, c1, r2, c2 in queries:
        answer.append(rotate(r1-1, c1-1, r2-1, c2-1))
    return answer