import io
import sys

_INPUT = """\
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
"""
sys.stdin = io.StringIO(_INPUT)

class Queue():
    def __init__(self,MAX):
       self.head = 0
       self.tail = 0
       self.MAX = MAX
       self.value = [[None,None]]*(self.MAX+1)
    def isEmpty(self):
        return self.head == self.tail
    def isFull(self):
        return self.head == (self.tail+1) % (self.MAX+1)
    
    def enqueue(self,x):
        if self.isFull():
            print('Queue is Full')
        else:
            if self.tail == self.MAX+1:
                self.tail = 0
            self.value[self.tail] = x
            self.tail +=1
    
    def dequeue(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            x = self.value[self.head]
            if self.head == self.MAX:
                self.head = 0
            else:
                self.head+=1
            return x

def min(a,b):
    return a if a < b else b

elaps = 0
nq = input().split(' ')
n = int(nq[0])
q = int(nq[1])
Q = Queue(n)
for i in range(n):
    nametime = input().split(' ')
    Q.value[i] = [nametime[0],int(nametime[1])]

Q.head = 0
Q.tail = n

while Q.head != Q.tail:
    u = Q.dequeue()
    c = min(q,u[1])
    u[1] -= c
    elaps += c
    if u[1] > 0:
        Q.enqueue(u)
    else:
        print(u[0],elaps)

