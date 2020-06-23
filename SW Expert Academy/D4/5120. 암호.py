import sys
sys.stdin = open('5120 암호.txt','r')

class Node:
    def __init__(self,d=0,p=None,n=None):
        self.data = d
        self.prev = p
        self.next = n
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
def addLast(lst,new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev    #head의 이전 것을 tail인것처럼 생각하자
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1
def printList(lst):
    if lst.head is None : return
    cur = lst.head.prev
    cycle = 10 if lst.size >= 10 else lst.size
    for _ in range(cycle):
        print(cur.data, end=' ')
        cur = cur.prev
    print()


T = int(input())
for tc in range(T):
    N, M, K = map(int,input().split())
    mylist = LinkedList()
    input_data = list(map(int,input().split()))
    for i in input_data:
        addLast(mylist,Node(i))
    cur = mylist.head
    for _ in range(K):
        for _ in range(M):
            cur = cur.next
        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new
        mylist.size += 1
    print('#{}'.format(tc+1),end=" ");printList(mylist)

