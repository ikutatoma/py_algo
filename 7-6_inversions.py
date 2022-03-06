import io
import sys
import math
__INPUT = """\
5
3 5 2 1 4
"""
sys.stdin = io.StringIO(__INPUT)

def merge(A,n,left,mid,right):
    cnt = 0
    n1 = mid - left
    n2 = right - mid
    L = [None]*n1
    R = [None]*n2
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L.append(MAX)
    R.append(MAX)
    i = j = 0
    for k in range(left,right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j += 1
            cnt+= n1 - i
    return cnt

def merge_sort(A,n,left,right):
    if left + 1 < right:
        mid = math.floor((left + right) / 2)
        v1 = merge_sort(A,n,left,mid)
        v2 = merge_sort(A,n,mid,right)
        v3 = merge(A,n,left,mid,right)
        return v1 + v2 + v3
    else:
        return 0
MAX = 100
n = int(input())
A = input().split(" ")
A = list(map(int,A))
ans = merge_sort(A,n,0,n)
print(ans)