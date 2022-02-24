import io
import sys
__INPUT = """\
5
1 5 7 10 21
4
2 4 17 8
"""
sys.stdin = io.StringIO(__INPUT)

def exhaustive_sarch(i,m):
    if m == 0:
        return True
    if i >= n:
        return False
    res = exhaustive_sarch(i + 1, m) or exhaustive_sarch(i + 1, m - int(A[i]))
    return res

n = int(input())
A = input().split(' ')
q = int(input())
M = input().split(' ')
for m in M:
    print(exhaustive_sarch(0,int(m)))