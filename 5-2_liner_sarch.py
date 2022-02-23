import io
import sys
_INPUT = """\
5
1 2 3 4 5
3
3 4 1
"""
sys.stdin = io.StringIO(_INPUT)

def liner_sarch1(A,key):
    for i in range(n):
        if A[i]==key:
            return i
    return 'NOT_FOUND'

def liner_sarch2(A,key):
    i=0
    A.append(key)
    while A[i]!=key:
        i+=1
    if i==n:
        return 'NOT_FOUND'
    return i

n=int(input())
S=input().split(' ')
q=int(input())
T=input().split(' ')
sum_1 = 0
sum_2 = 0
for i in range(q):
    if liner_sarch1(S,T[i]) != 'NOT_FOUND':
        sum_1+=1
    if liner_sarch2(S,T[i]) != 'NOT_FOUND':
        sum_2 +=1
print(sum_1,sum_2)