import io
import sys
__INPUT = """\
12
13 19 9 5 12 8 7 4 21 2 6 11
"""
sys.stdin = io.StringIO(__INPUT)

def partition(p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i+=1
            t = A[i]
            A[i] = A[j]
            A[j] = t
    t = A[i + 1]
    A[i + 1] = A[r]
    A[r] = t
    return i + 1

n = int(input())
A =  input().split(' ')
for i in range(len(A)):
    A[i] = int(A[i])

q = partition(0,n-1)

for i in range(n):
    if i == q:
        print("[",end=" ")
    print(A[i],end=" ")
    if i == q:
        print("]",end=" ")
print("\n")