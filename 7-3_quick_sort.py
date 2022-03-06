import io
import sys
__INPUT = """\
6
D 3
H 2
D 1
S 3
D 2
C 1
"""
sys.stdin = io.StringIO(__INPUT)

def partition(A,p,r):
    x = A[r][1]
    i = p - 1
    for j in range(p,r):
        if A[j][1] <= x:
            i += 1
            A[i][1],A[j][1] = A[j][1],A[i][1]
    t = A[i + 1]
    A[i + 1] = A[r]
    A[r] = t
    return i + 1


def quick_sort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

n = int(input())
A = [0]*n
for i in range(n):
    A[i] = input().split(' ')
    A[i][1] = int(A[i][1])
quick_sort(A,0,n-1)
print(A)