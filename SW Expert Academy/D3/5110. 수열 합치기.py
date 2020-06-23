import sys
sys.stdin = open('5110. 수열 합치기.txt','r')

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
def addList(lst,arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new
    if lst.head is None:                    #만약 기존 연결리스트가 비어있다면(즉 처음 수열을 넣는거라면)
        lst.head, lst.tail = first, last    #수열의 앞 뒤 부분을 연결리스트 앞, 뒤에 연결
    else:
        cur = lst.head                      #수열에 또 다른 수열을 추가하는 일을하면 이전의 순열을 앞에서부터 탐색
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None: #뒤에 추가
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last                 #합쳤으니까 연결리스트의 tail은 last임
        elif cur.prev is None : #앞에 추가   
            last.next = lst.head
            lst.head.prev = last
            lst.head = first               #합쳤으니까 연결리스트의 head는 first임
        else: #중간에 추가
            prev = cur.prev
            last.next = cur
            prev.next = first
            cur.prev = last
            first.prev = prev
    lst.size += len(arr)
def printList(lst):
    if lst.head is None: return
    prev, cur = None, lst.head
    # while cur is not None:
    #     print(cur.data, end=" ")
    #     cur = cur.next
    # print()
    cur = lst.tail
    # while cur is not None:
    for _ in range(10):
        print(cur.data, end=" ")
        cur = cur.prev
    print()
T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    mylist = LinkedList()
    for m in range(M):
        addList(mylist,list(map(int,input().split())))
    print('#{}'.format(tc+1),end=" ");printList(mylist)


