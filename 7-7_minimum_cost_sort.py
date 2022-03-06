import io
import sys
__INPUT = """\
5
1 5 3 4 2
"""
sys.stdin = io.StringIO(__INPUT)

def solve(A,B,T,n):
    ans = 0
    V = [False]*n
    for i in range(n):
        B[i] = A[i]
    B.sort()
    for i in range(n):
        T[B[i]] = i
    for i in range(n):
        if V[i]:
            continue
        cur = i
        S = 0
        m = VMAX
        an = 0
        while 1:
            V[cur] = True
            an+=1
            v = A[cur]
            m = min(m,v)
            S += v
            cur = T[v]
            if V[cur]:
                break
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)
    return ans

MAX = 100
VMAX = 100
n = int(input())
A = input().split(' ')
B = [None]*n
T = [None]*(n+1)
s = VMAX
for i in range(n):
    A[i] = int(A[i])
    s = min(s,A[i])
ans = solve(A,B,T,n)
print(ans)