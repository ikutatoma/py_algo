import io
import sys
__INPUT = """\
7
2 5 1 3 2 3 0
"""
sys.stdin = io.StringIO(__INPUT)

def counting_sort(A,n,k):
    B = [0]*(n+1)
    C = [0]*(k+1)
    for j in range(n):
        C[A[j]]+=1
    for i in range(1,k+1):
        C[i] += C[i - 1]
    for j in reversed(range(n)):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
    return B

n = int(input())
A = input().split(' ')
A = list(map(int,A))
k = max(A)
b = counting_sort(A,n,k)
for i in range(1,n+1):
    print(b[i],end=" ")
print()


