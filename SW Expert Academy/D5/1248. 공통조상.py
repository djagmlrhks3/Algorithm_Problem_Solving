import sys
sys.stdin = open('1248. 공통조상.txt', 'r')

#서브트리의 노드 수를 계산하는 함수
def solution(node):
    global count
    if node != 0:
        count+=1
        solution(matrix[node][1])
        solution(matrix[node][2])

#조상을 찾아주는 함수
def find(node, flag):
    global parent
    #N1의 조상을 찾아주는 파트
    if flag and node!=0:
        mother.append(node)
        find(matrix[node][3], True)
    #N2와 N1의 가장가까운 부모를 찾아주는 파트
    if not flag and node!=0:
        if node in mother:parent=node;return
        find(matrix[node][3], False)

T = int(input())
for tc in range(T):
    V, E, N1, N2 = map(int,input().split())
    data = list(map(int, input().split()))

    matrix = [[i, 0, 0, 0] for i in range(0, V+1)]
    for x in range(0,E):
        s, e = data[2*x], data[2*x+1]
        #이진트리에서 1번부분이 채워져있다면 2번부분으로 채운다.
        if not matrix[s][1]:
            matrix[s][1] = e
        else:
            matrix[s][2] = e
        #3번째 인덱스에 부모를 입력.
        matrix[e][3] = s
    parent = '' #가장 가까운 부모를 담는 변수
    count = 0   #서브트리 수를 담는 변수
    mother = []  #N1의 부모를 담는 리스트
    find(N1, True)
    find(N2, False)
    solution(parent)
    print('#{} {} {}'.format(tc+1, parent, count))
