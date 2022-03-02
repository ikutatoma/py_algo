import math
import io
import sys
__INPUT = """\
10
8 5 9 2 6 3 7 1 10 4
"""

sys.stdin = io.StringIO(__INPUT)

def merge(left,mid,right):
    global cnt
    n1 = mid - left
    n2 = right - mid
    L = [None]*n1
    R = [None]*n2
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L.append(INFTY)
    R.append(INFTY)
    i = 0
    j = 0
    print(L,R,left,right)
    for k in range(left, right):
        cnt+=1
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def merge_sort(left,right):
    if left + 1 < right:
        mid = math.floor((left + right)/ 2 )
        merge_sort(left,mid)
        merge_sort(mid,right)
        merge(left,mid,right)

cnt = 0
INFTY = 100000
n = int(input())
A = input().split(" ")
for i in range(n):
    A[i] = int(A[i])

merge_sort(0,n)
for i in range(n):
    print(str(A[i]),end=" ")
print("\n" + str(cnt))