import sys
sys.stdin = open('5122. 수열 편집.txt','r')
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
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
        if L >= self.size:
            print(-1)
        else:
            prev, cur = None, self.head
            for _ in range(L):
                prev = cur
                cur = cur.next
            print(cur.data)
    def change(self,idx,val):
        prev, cur = None, self.head
        for _ in range(idx):
            prev = cur
            cur = cur.next
        cur.data = val
    def deleteAt(self,idx):
        if self.head is None:
            print('빈 리스트에서 삭제는 안됩니다!')
        else:
            prev, cur = None, self.head
            for _ in range(idx):
                prev = cur
                cur = cur.next
            if prev is None:
                del self.head
                self.head = self.tail = None
            else:
                prev.next = cur.next
                del cur
            self.size -= 1

# def I(location,number):
#     input_data.insert(location,number)
# def D(location):
#     input_data.pop(location)
# def C(location,number):
#     input_data[location] = number
T = int(input())
for tc in range(T):
    N, M, L = map(int,input().split())
    input_data = list(map(int,input().split()))
    mylist = List()
    for i in input_data:
        mylist.insertlast(i)
    for m in range(M):
        order, *args = input().split()
        if order == "I":
            mylist.insertAt(int(args[0]),int(args[1]))
        elif order == "D":
            mylist.deleteAt(int(args[0]))
        elif order == "C":
            mylist.change(int(args[0]),int(args[1]))
    print('#{}'.format(tc+1),end=" ")
    mylist.result()
