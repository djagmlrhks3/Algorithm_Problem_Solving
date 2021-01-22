import sys
sys.stdin = open('백준10825. 국영수.txt', 'r')

students = []
N = int(input())
for _ in range(N):
    name, kor, eng, mat = sys.stdin.readline().split()
    students.append((name, int(kor), int(eng), int(mat)))


students = sorted(students, key=lambda x: [-x[1], x[2], -x[3], x[0]])

for student in students:
    print(student[0])