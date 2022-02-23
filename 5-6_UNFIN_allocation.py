import io
import sys
import math
__INPUT = """\
5 3
3
6
7
8
9
"""
sys.stdin = io.StringIO(__INPUT)

def bubble_sort(a):
    flag = 1
    i = 0
    l = len(a)
    while flag:
        flag = 0
        for j in reversed(range(i+1,l)):
            if a[j]< a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
                flag = 1
        i+=1
    return a

def check(P):
    i = 0
    for j in range(k):
        s = 0
        while (s+T[i]) <= P:
            s += T[i]
            i+=1
            if i == n:
                return n
    return i

def solve():
    left = 0
    right = 100*100
    while right - left > 1:
        mid = math.floor((right + left)/2)
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid

    return right 


MAX = 10000
n,k = input().split(" ")
n,k = int(n),int(k)
T = [int(input()) for i in range(n)]
T = bubble_sort(T)
print(T,n,k)
ans = solve()
print(ans)


