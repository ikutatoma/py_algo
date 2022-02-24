import io
import sys
import math
__INPUT = """\
1 100 5 2 0
0 5
"""
sys.stdin = io.StringIO(__INPUT)

def max(x,y):
    return x if x > y else y

def findMaximum(A,l,r):
    m = math.floor((l + r)/2)
    if l == r-1:
        return int(A[l])
    else:
        u = findMaximum(A,l,m)
        v = findMaximum(A,m,r)
        x = max(u,v)
    return x

A = input().split(' ')
l,r = input().split(' ')
print(findMaximum(A,int(l),int(r)))