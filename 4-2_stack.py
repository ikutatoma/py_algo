import io
import sys

_INPUT = """\
1 2 + 3 4 - *
"""
sys.stdin = io.StringIO(_INPUT)
class Stack():
    def __init__(self,MAX):
        self.top = 0
        self.MAX = MAX
        self.value = [None]*self.MAX        
    def isEmpty(self):
        return self.top == 0
    def isFull(self):
        return self.top >= self.MAX-1
    def push(self,x):
        if self.isFull():
            print('Stack is Full')
        self.top+=1
        self.value[self.top]=x
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
        self.top-=1
        return self.value[self.top+1];


S = Stack(6)

s = input().split(' ')
for i in s:
    if i == '+':
        a = int(S.pop());
        b = int(S.pop());
        S.push(a+b);
    elif i == '-':
        b = int(S.pop());
        a = int(S.pop());
        S.push(a-b);
    elif i == '*':
        a =int(S.pop());
        b = int(S.pop());
        S.push(a*b);
    else:
        S.push(i);

print(S.pop())
