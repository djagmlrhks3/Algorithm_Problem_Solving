import sys
sys.stdin = open('5108. 숫자 추가.txt','r')
"""
N : 수열 길이
M : 추가 횟수
L : 인덱스번호
"""

# T = int(input())
# for tc in range(T):
#     N, M, L = map(int,input().split())
#     input_data = list(map(int,input().split()))
#     for m in range(M):
#         location, number = map(int,input().split())
#         input_data.insert(location,number)
#
#     print('#{} {}'.format(tc+1,input_data[L]))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    # def __del__(self):
    #     print(self.data, '삭제')
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def printlist(self):
        if self.size == 0:
            print('빈 리스트...')
            return
        cur = self.head
        print(self.size, '[', end=' ')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')
    def insertfirst(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    def insertlast(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
    def insertAt(self, idx, val):
        if self.head is None or idx==0:
            self.insertfirst(val)
            return
        if self.size <= idx:
            self.insertlast(val)
            return
        prev, cur = None, self.head
        for i in range(idx):
            prev = cur
            cur = cur.next
        node = Node(val)
        node.next = prev.next
        prev.next = node
        self.size += 1
    def deletefirst(self):
        if self.head is None:
            print('빈 리스트...')
            return
        if self.head is self.tail:
            del self.head
            self.head = self.tail = None
        else:
            cur = self.head
            self.head = cur.next
            del cur
        self.size -= 1
    def deletelast(self):
        if self.head is None:
            print('빈 리스트...')
            return
        prev, cur = None, self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next
        if prev is None:
            del self.head
            self.head = self.tail = None
        else:
            prev.next = None
            del self.tail
            self.tail = prev
        self.size -= 1
    def result(self):
        prev, cur = None, self.head
        for _ in range(L):
            prev = cur
            cur = cur.next
        print(cur.data)
T = int(input())
for tc in range(T):
    N, M, L = map(int,input().split())
    input_data = list(map(int,input().split()))
    mylist = List()
    for i in input_data:
        mylist.insertlast(i)
    for m in range(M):
        idx, new = map(int, input().split())
        mylist.insertAt(idx,new)
    print('#{}'.format(tc+1),end=" ")
    mylist.result()