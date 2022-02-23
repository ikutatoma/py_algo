import io
import sys
import math
__INPUT = """\
5
1 2 3 4 5
3
3 4 1
"""
sys.stdin = io.StringIO(__INPUT)

def binary_sarch(A,key):
    left = 0
    right = len(A)
    while left < right:
        mid = math.floor((left+right)/2)
        if A[mid] ==key:
            return mid
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return 'NOT_FOUND'

n=int(input())
S=input().split(' ')
q=int(input())
T=input().split(' ')
sum = 0
for i in range(q):
    if binary_sarch(S,T[i]) != 'NOT_FOUND':
        sum+=1
print(sum)